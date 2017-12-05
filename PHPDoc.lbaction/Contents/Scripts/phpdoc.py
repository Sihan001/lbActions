#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import urllib2
import urllib
import tempfile
import os

items = []
item = {}

tqfile = os.path.join(tempfile.gettempdir(), 'phpdocdata.txt')
tqurl = 'http://php.net/js/search-index.php?lang=en'
keyword = "".join(sys.argv[1:])
phpdoc = ''

if os.path.isfile(tqfile):
	with open(tqfile, "r") as fp:
		phpdoc = fp.read()
else:
	res = urllib2.Request(tqurl)
	response = urllib2.urlopen(res)	
	phpdoc = response.read()
	response.close()
	with open(tqfile, "w") as fp:
		fp.write(phpdoc)

entries = json.loads(phpdoc)

for entrie in entries:
	if keyword == entries[entrie][0][0:len(keyword)]:
		item = {}
		item['title'] = entries[entrie][0]
		item['subtitle'] = entries[entrie][1]
		item['url'] = "http://php.net/manual/en/%s.php" % entries[entrie][0]
		items.append(item)

if not items:
	item = {}
	item['title'] = 'No matches found'
	item['subtitle'] = 'No matches found'
	item['icon'] = "icon.png"
	items.append(item)

print json.dumps(items)
