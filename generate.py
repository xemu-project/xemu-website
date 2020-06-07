#!/usr/bin/env python
"""
xemu.app Static Site Generator
"""

import codecs
import json
import os
import re
import requests

from collections import defaultdict
from datetime import datetime, timezone
from github import Github
from jinja2 import Environment, FileSystemLoader
from tqdm import tqdm

output_dir = 'dist'
repo_url_base = 'https://raw.githubusercontent.com/mborgerson/xemu-website/master/'
compatibility_reports_url = 'https://reports.xemu.app/compatibility'
compatibility_reports_url_verify_certs = True
# compatibility_reports_url = 'https://127.0.0.1/compatibility'
# compatibility_reports_url_verify_certs = False

title_status_descriptions = {
    'Unknown'  : 'A compatibility test has not been recorded for this title.',
    'Broken'   : 'This title crashes very soon after launching, or displays nothing at all.',
    'Intro'    : 'This title displays an intro sequence, but fails to make it to gameplay.',
    'Starts'   : 'This title starts, but may crash or have significant issues.',
    'Playable' : 'This title is playable from start to finish, with only minor issues.',
    'Perfect'  : 'This title is playable from start to finish with no noticable issues.'
    }

def get_field(s,x):
    return s[x] if x in s else ''

class Issue:
    all_issues = []
    issues_by_title = defaultdict(list)

    def __init__(self, number, url, title, affected_titles, created_at, updated_at):
        self.number = number
        self.url = url
        self.title = title
        self.affected_titles = affected_titles
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return self.title

    @classmethod
    def load_issues(cls, title_alias_map):
        """
        Search through all GitHub issues for any title tags to construct a
        list of titles and their associated issues
        """
        titles_re = re.compile(r'Titles?:\s*([a-fA-f0-9,\s]+)')
        title_id_re = re.compile(r'([a-fA-f0-9]{8})')
        for issue in Github().get_user('mborgerson').get_repo('xemu').get_issues():
            if issue.state != 'open': continue
            # Look for a titles sequence and pull out anything that looks like
            # an id
            references = ' '.join(titles_re.findall(issue.body))
            affected_titles = title_id_re.findall(references)
            cls.all_issues.append(cls(
                issue.number,
                issue.html_url,
                issue.title,
                affected_titles,
                issue.created_at,
                issue.updated_at))

        # Organize issues by title
        for issue in cls.all_issues:
            for title_id in issue.affected_titles:
                if title_id not in title_alias_map:
                    print('Warning: Issue %s references unknown title id "%s"' % (issue.url, title_id))
                    continue
                if issue not in cls.issues_by_title[title_alias_map[title_id]]:
                    cls.issues_by_title[title_alias_map[title_id]].append(issue)

class CompatibilityReport:
    all_reports = []
    reports_by_title = defaultdict(list)

    def __init__(self, info):
        self.info = info

    @property
    def created_at(self):
        return datetime.fromtimestamp(self.info['created_at'], timezone.utc)

    @classmethod
    def load_reports(cls, title_alias_map, url, verify):
        # FIXME: Ideally shouldn't load this all into memory. Instead, save to
        # disk and load on demand. But this works for now.
        cls.all_reports = [CompatibilityReport(i) for i in json.loads(requests.get(url, verify=verify).text)]
        for report in cls.all_reports:
            title_id = '%08x' % report.info['xbe_cert_title_id']
            if title_id not in title_alias_map:
                print('Warning: Compatibility report %s references unknown title "%s"' % (report.info['_id'], title_id))
                continue
            cls.reports_by_title[title_alias_map[title_id]].append(report)

class Title:
    def __init__(self, info_path):
        with open(info_path) as f:
            self.info = json.load(f)
        self.pubid = codecs.decode(self.info['title_id'][0:4], 'hex').decode('ascii')
        self.tid = '%03d' % (int(self.info['title_id'][4:], 16))
        self.title_url = f"/titles/{self.info['title_id']}"
        self.title_path = os.path.dirname(info_path)
        self.title_name = self.info['name']
        self.full_title_id_text = '%s-%s' % (self.pubid, self.tid)
        self.full_title_id_hex = self.info['title_id']

        # Determine cover paths
        self.have_cover = True
        self.cover_path = f'cover_front.jpg'
        if not os.path.exists(os.path.join(self.title_path, self.cover_path)):
            # Try .png extension
            self.cover_path = f'cover_front.png'
            if not os.path.exists(os.path.join(self.title_path, self.cover_path)):
                self.have_cover = False
        
        self.have_thumbnail = True
        self.cover_thumbnail_path = 'cover_front_thumbnail.jpg'
        if not os.path.exists(os.path.join(self.title_path, self.cover_thumbnail_path)):
            assert not self.have_cover, "Please create thumbnail for %s" % self.title_name
            self.have_thumbnail = False

        if self.have_cover:
            self.cover_url = repo_url_base + self.title_path + '/' + self.cover_path
        else:
            print('Note: Missing artwork for %s' % self.title_name)
            self.cover_url = repo_url_base + '/cover_front_default.png'

        if self.have_thumbnail:
            self.cover_thumbnail_url = repo_url_base + self.title_path + '/' + self.cover_thumbnail_path
        else:
            if self.have_cover:
                print('Note: Missing thumbnail for %s' % self.title_name)
            self.cover_thumbnail_url = self.cover_url

    def process_compatibility(self):
        # FIXME:
        # - Only show reports for master branch
        # - Sort by the build version that was tested, showing most recent
        #   builds first
        # - Check version against repo for version numbers to filter out
        #   unofficial builds
        self.compatibility_tests = CompatibilityReport.reports_by_title[self.full_title_id_hex]
        if len(self.compatibility_tests) > 0:
            self.most_recent_test = sorted(self.compatibility_tests, key=lambda x:x.info['created_at'])[-1]
            self.status = self.most_recent_test.info['compat_rating']
            assert(self.status in title_status_descriptions)
        else:
            self.most_recent_test = None
            self.status = 'Unknown'
        assert(self.status in title_status_descriptions)

    @property
    def issues(self):
        return Issue.issues_by_title[self.info['title_id']]

def main():
    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    game_status_counts = {
        'Unknown'  : 0,
        'Broken'   : 0,
        'Intro'    : 0,
        'Starts'   : 0,
        'Playable' : 0,
        'Perfect'  : 0,
    }

    print('Gathering info.json files...')
    titles = []
    title_alias_map = {}
    title_lookup = {}
    for root, dirs, files in os.walk('titles', topdown=True):
        for name in files:
            if name != 'info.json': continue
            title = Title(os.path.join(root,name))
            titles.append(title)
            assert(title.full_title_id_hex not in title_lookup), "Title %s defined in multiple places" % title.full_title_id_hex
            title_lookup[title.full_title_id_hex] = title
            for release in title.info['releases']:
                title_alias_map[release['title_id']] = title.info['title_id']
    print('  - Found %d' % (len(titles)))

    print('Getting GitHub Issues List...')
    # Issue.load_issues(title_alias_map)
    print('  - Ok. %d issues total' % len(Issue.all_issues))

    print('Getting compatibility report list...')
    CompatibilityReport.load_reports(
        title_alias_map,
        compatibility_reports_url,
        compatibility_reports_url_verify_certs
        )
    print('  - Ok. %d reports total' % len(CompatibilityReport.all_reports))
    for title in titles:
        title.process_compatibility()
        game_status_counts[title.status] += 1

    print('Rebuilding pages...')
    template = env.get_template('template_title.html')
    count = 0
    for title_id in tqdm(title_lookup):
        title_dir = os.path.join(output_dir, 'titles', title_id)
        os.makedirs(title_dir, exist_ok=True)
        title = title_lookup[title_id]
        with open(os.path.join(title_dir, 'index.html'), 'w') as f:
            f.write(template.render(
                title=title,
                title_status_descriptions=title_status_descriptions
                ))
        count += 1
    print('  - Created %d title pages' % count)

    print('Generating alias redirects...')
    count = 0
    for title_id in title_alias_map:
        if title_alias_map[title_id] != title_id:
            # This is an alias, create a redirect
            title_dir = os.path.join(output_dir, 'titles', title_id)
            os.makedirs(title_dir, exist_ok=True)
            with open(os.path.join(title_dir, 'index.html'), 'w') as f:
                url=f"/titles/{title_alias_map[title_id]}"
                f.write(f'<html><head><meta http-equiv="refresh" content="0; URL={url!s}" /></head></html>')
            count += 1
    print('  - Created %d redirect pages' % count)

    print('Rebuilding index...')
    template = env.get_template('template_index.html')
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(template.render(
            titles=sorted(titles,key=lambda title:title.title_name),
            title_status_descriptions=title_status_descriptions,
            game_status_counts=game_status_counts
            ))
    print('  - Ok')

if __name__ == '__main__':
    main()
