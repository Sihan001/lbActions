#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import urllib
import urllib2

API = "01068bdd0c3168a70313a397249439f5"
URL = "https://api.douban.com/v2/book/search?count=20&"

items = []
item = {}

keyword = "".join(sys.argv[1:])
if not keyword:
	sys.exit()

query = urllib.urlencode({'apikey': API, 'q': keyword})
api_url = URL + query
res = urllib2.Request(api_url)
response = urllib2.urlopen(res)
html = response.read()
response.close()
if not html:
    sys.exit()

resultList = json.loads(html)

for music in resultList['books']:
	item = {}
	item['title'] = music['title']
	item['subtitle'] = u'作者: ' + ",".join(music['author']) + u' 评分: ' + str(music['rating']['average']) + '/' + str(music['rating']['numRaters'])
	item['icon'] = 'C5C34466-B858-4F14-BF5E-FD05FA0903DA.png'
	item['url'] = music['alt']
	item['quickLookURL'] = music['alt']
	items.append(item)

print json.dumps(items)
