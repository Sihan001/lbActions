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
URL = "https://api.douban.com/v2/movie/search?count=20&"

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

for music in resultList['subjects']:
	item = {}
	item['title'] = music['title']
	item['subtitle'] = u'年份: ' + music['year'] + u' 评分: ' + str(music['rating']['average']) + ',' + u' 类型: ' + music['subtype'] + u' 别名: ' + music['original_title']
	item['icon'] = '4E86472A-FB8F-4F64-975F-785BF66B9F08.png'
	item['url'] = music['alt']
	item['quickLookURL'] = music['alt']
	items.append(item)

print json.dumps(items)
