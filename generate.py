#!/usr/bin/env python3
import codecs
import csv
import json
import os
import re
from tqdm import tqdm
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

cover_path_url_base = 'https://raw.githubusercontent.com/mborgerson/xemu-website/master/'
web_root = 'https://mborgerson.github.io/xemu-website/'

titles = {}
bad_titles = []
title_status_descriptions = {
	'Unknown'  : 'A compatibility test has not been recorded for this title.',
	'Broken'   : 'This title crashes very soon after launching, or displays nothing at all.',
	'Intro'    : 'This title displays an intro sequence, but fails to make it to gameplay.',
	'Starts'   : 'This title starts, but may crash or have significant issues.',
	'Playable' : 'This title is playable from start to finish, with only minor issues.',
	'Perfect'  : 'This title is playable from start to finish with no noticable issues.'
	}
title_status_names = [
	'Unknown',
	'Broken',
	'Intro',
	'Starts',
	'Playable',
	'Perfect',
	]
title_status_colors = {
	'Unknown'  : '#2A2A2A',
	'Broken'   : '#D7263D',
	'Intro'    : '#F86624',
	'Starts'   : '#FF9800',
	'Playable' : '#1B998B',
	'Perfect'  : '#4CAF50',
	}

class TitleRelease:
	def __init__(self, title,region,edition,xboxid,pubid,titleid,discid,regionid):
		self.title = title
		self.region = region
		self.edition = edition
		self.xboxid = xboxid
		self.pubid = pubid
		self.titleid = titleid
		self.discid = discid
		self.regionid = regionid

def load_title_db():
	global titles
	with open('db.csv') as f:
		for row in csv.reader(f):
			title,region,edition,xboxid,pubid,titleid,discid,regionid = row
			# Don't catalog rows with invalid publisher, title, or title info
			is_bad = True
			try:
				int(titleid)
				is_bad = False
			except:
				pass
			if title == '' or pubid == '' or titleid == '' or is_bad:
				continue
			full_titleid = (pubid,titleid)
			if full_titleid not in titles:
				titles[full_titleid] = []
			titles[full_titleid].append(TitleRelease(*row))

def get_field(s,x):
	return s[x] if x in s else ''

class CompatibilityTest:
	def __init__(self, d):
		timef = '%Y-%m-%d %H:%M:%S %Z'
		self.tester = get_field(d, "tester")
		self.date = datetime.strptime(get_field(d, "date"), timef)
		self.build = get_field(d, "build")
		self.video = get_field(d, "video")
		self.platform = get_field(d, "platform")
		self.cpu = get_field(d, "cpu")
		self.gfx_card = get_field(d, "gfx_card")
		self.gfx_driver = get_field(d, "gfx_driver")
		self.memory = get_field(d, "memory")
		self.xbe_hash = get_field(d, "xbe_hash")
		self.xbe_version = get_field(d, "xbe_version")
		self.xbe_region = get_field(d, "xbe_region")
		self.description = get_field(d, "description")
		self.rating = get_field(d, "rating")

class Title:
	def __init__(self, pubid, tid):
		self.pubid = pubid
		self.tid = tid
		pub_hex = codecs.encode(pubid.encode('ascii'), 'hex').decode('ascii')

		# Determine cover paths
		self.title_path = os.path.join('titles', pubid, tid)
		self.cover_path = os.path.join(self.title_path, 'cover_front.jpg')
		self.have_cover = True
		if not os.path.exists(self.cover_path):
			self.cover_path = os.path.join(self.title_path, 'cover_front.png')
			if not os.path.exists(self.cover_path):
				self.have_cover = False
				self.cover_path = 'cover_front_default.png'
		
		self.cover_thumbnail_path = os.path.join(self.title_path, 'cover_front_thumbnail.jpg')
		if not os.path.exists(self.cover_thumbnail_path):
			self.cover_thumbnail_path = 'cover_front_default.png'

		self.cover_url = cover_path_url_base + self.cover_path
		self.cover_thumbnail_url = cover_path_url_base + self.cover_thumbnail_path

		self.title_url = f'./{self.pubid}/{self.tid}.html'

		# Get title info
		info_path = os.path.join(self.title_path, 'info.json')
		self.title_report = {}
		if os.path.exists(info_path):
			with open(info_path) as f:
				# Strip comments from lines
				lines = '\n'.join(['' if re.match(r'^\s*//.+', l) else l for l in f])
				self.title_report = json.loads(lines)

		# Get all known releases of the game
		self.releases = titles[(pubid, tid)]

		# Determine which title name should be displayed
		self.title_name = get_field(self.title_report, 'display_title') or self.releases[0].title
		self.full_title_id_text = '%s-%s' % (pubid, tid)
		self.full_title_id_hex = '%s%04x' % (pub_hex, int(tid))

		# Parse out compatibility tests
		self.compatibility_tests = []
		self.most_recent_test = None
		if 'compatibility_tests' in self.title_report:
			self.compatibility_tests = [CompatibilityTest(x) for x in self.title_report['compatibility_tests']]
		if len(self.compatibility_tests) > 0:
			self.most_recent_test = compatibility_tests[-1]

		if self.most_recent_test:
			self.status = self.most_recent_test.rating
		else:
			self.status = 'Unknown'
		assert(self.status in title_status_descriptions)

def main():
	load_title_db()
	output_dir_path = 'dist'
	os.makedirs(output_dir_path, exist_ok=True)

	print('Generating webpages...')
	index_titles = []
	game_status_counts = {
		'Unknown'  : 0,
		'Broken'   : 0,
		'Intro'    : 0,
		'Starts'   : 0,
		'Playable' : 0,
		'Perfect'  : 0,
	}

	env = Environment(loader=FileSystemLoader(searchpath='templates'))

	for pubid, tid in tqdm(titles):
		title = Title(pubid, tid)
		index_titles.append(title)

		# Update global stats
		game_status_counts[title.status] += 1

		# Generate page
		os.makedirs(os.path.join(output_dir_path, pubid), exist_ok=True)
		output_page_path = os.path.join(output_dir_path, pubid, tid + ".html")
		template = env.get_template('template_title.html')
		open(output_page_path, 'w').write(template.render(**locals(), **globals()))

	# Generate index
	output_page_path = os.path.join(output_dir_path, 'index.html')
	template = env.get_template('template_index.html')
	open(output_page_path, 'w').write(template.render(**locals(), **globals()))

if __name__ == '__main__':
	main()
