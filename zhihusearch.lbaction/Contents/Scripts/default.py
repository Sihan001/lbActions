#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import urllib2
import urllib

item = {}
items = []
keyword = "".join(sys.argv[1:])
ZHDAILY_API = 'http://news.at.zhihu.com/api/1.2/news/latest'
ZHSEARCH_API = 'http://www.zhihu.com/autocomplete?max_matches=10&use_similar=0&'
if not keyword:
	res = urllib2.Request(ZHDAILY_API)
	response = urllib2.urlopen(res)
	data = response.read()
	response.close()
	dailyLists = json.loads(data)
	for daily in dailyLists['news']:
		item = {}
		item['title'] = daily['title']
		item['subtitle'] = daily['share_url']
		item['url'] = daily['share_url']
		item['quickLookURL'] = daily['share_url']
		items.append(item)
	print json.dumps(items)
else:
	query = urllib.urlencode({'token': keyword})
	res = urllib2.Request(ZHSEARCH_API + query)
	response = urllib2.urlopen(res)
	data = response.read()
	response.close()
	sugLists = json.loads(data)
	for sug in sugLists[0]:
		if sug == 'entry' or sug[0] == 'search_link':
			continue
		if sug[0] == 'question':
			link = 'http://www.zhihu.com/%s/%s' % (sug[0], sug[3])
		elif sug[0] == 'article':
			link = 'https://zhuanlan.zhihu.com/p/%s' % sug[3]
		else:
			link = 'http://www.zhihu.com/%s/%s' % (sug[0], sug[2])
		item = {}
		item['title'] = sug[1]
		item['subtitle'] = sug[0]
		item['url'] = link
		item['quickLookURL'] = link
		item['icon'] = '%s.png' % sug[0]
		items.append(item)
	print json.dumps(items)
