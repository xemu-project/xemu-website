#!/usr/bin/env python
import codecs
import json
import os
import re

from collections import defaultdict
from datetime import datetime
from github import Github
from jinja2 import Environment, FileSystemLoader
from tqdm import tqdm

repo_url_base = 'https://raw.githubusercontent.com/mborgerson/xemu-website/master/'

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
    issues_by_title = None

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
    def get_all_issues(cls):
        """
        Search through all GitHub issues for any title tags to construct a list of
        titles and their associated issues
        """
        issues = []
        titles_re = re.compile(r'Titles?:\s*(\w+)(\s*,\s*\w+)*')
        for issue in Github().get_user('mborgerson').get_repo('xemu').get_issues():
            if issue.state != 'open': continue
            # Matches returns list of tuples, just concatenate everything, strip
            # out the comments and chop up by whitespace
            matches = titles_re.findall(issue.body)
            joiner = lambda x: ' '.join(x)
            matches = map(joiner, matches)
            affected_titles = []
            for t in joiner(matches).replace(',', ' ').split():
                affected_titles.append(t.lstrip('0x'))
            issues.append(cls(
                issue.number,
                issue.html_url,
                issue.title,
                affected_titles,
                issue.created_at,
                issue.updated_at))
        return issues

    @classmethod
    def get_issues_by_title(cls):
        if cls.issues_by_title is not None:
            return cls.issues_by_title

        # Organize issues by title
        issues_by_title = defaultdict(list)
        for issue in cls.get_all_issues():
            for title in issue.affected_titles:
                issues_by_title[title].append(issue)

        cls.issues_by_title = issues_by_title
        return issues_by_title

class CompatibilityTest:
    def __init__(self, d):
        timef = '%Y-%m-%d %H:%M:%S %Z'
        self.tester      = get_field(d, "tester")
        self.date        = datetime.strptime(get_field(d, "date"), timef)
        self.build       = get_field(d, "build")
        self.video       = get_field(d, "video")
        self.platform    = get_field(d, "platform")
        self.cpu         = get_field(d, "cpu")
        self.gfx_card    = get_field(d, "gfx_card")
        self.gfx_driver  = get_field(d, "gfx_driver")
        self.memory      = get_field(d, "memory")
        self.xbe_hash    = get_field(d, "xbe_hash")
        self.xbe_version = get_field(d, "xbe_version")
        self.xbe_region  = get_field(d, "xbe_region")
        self.description = get_field(d, "description")
        self.rating      = get_field(d, "rating")

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

        # Parse out compatibility tests
        self.compatibility_tests = []
        self.most_recent_test = None
        if 'compatibility_tests' in self.info:
            self.compatibility_tests = [CompatibilityTest(x) for x in self.info['compatibility_tests']]
        if len(self.compatibility_tests) > 0:
            self.most_recent_test = compatibility_tests[-1]
            self.status = self.most_recent_test.rating
        else:
            self.status = 'Unknown'
        assert(self.status in title_status_descriptions)

    @property
    def issues(self):
        return Issue.get_issues_by_title()[self.info['title_id']]

def main():
    output_dir = 'dist'
    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    game_status_counts = {
        'Unknown'  : 0,
        'Broken'   : 0,
        'Intro'    : 0,
        'Starts'   : 0,
        'Playable' : 0,
        'Perfect'  : 0,
    }

    # Gather all info.json files
    print('Gathering info.json files...')
    titles = []
    title_alias_map = {}
    title_lookup = {}
    for root, dirs, files in os.walk('titles', topdown=True):
        for name in files:
            if name != 'info.json': continue
            title = Title(os.path.join(root,name))
            titles.append(title)
            assert(title.full_title_id_hex not in title_lookup, "Title %s defined in multiple places" % title.full_title_id_hex)
            title_lookup[title.full_title_id_hex] = title
            game_status_counts[title.status] += 1
            for release in title.info['releases']:
                title_alias_map[release['title_id']] = title.info['title_id']
    print('  - Found %d' % (len(titles)))

    print('Getting GitHub Issues List...')
    Issue.get_all_issues()
    print('  - Ok')

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
