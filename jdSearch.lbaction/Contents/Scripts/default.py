#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import urllib2
import urllib

SUGURL = 'http://suggest-squanqiu.jd.com/?'
JDSEARCH = 'http://search.jd.com/Search?enc=utf-8&'

item = {}
items = []

keyword = sys.argv[1:]
keyword = "".join(keyword)
if not keyword:
	sys.exit()

sugurl = SUGURL + urllib.urlencode({'key': keyword})

res = urllib2.Request(sugurl)
response = urllib2.urlopen(res)
html = response.read()
response.close()
if not html:
    sys.exit()
sugList = json.loads(html)

item['title'] = keyword
url = JDSEARCH + urllib.urlencode({'keyword': keyword})
item['subtitle'] = u'京东搜索:' + keyword.decode("utf8")
item['url'] = url
item['quickLookURL'] = url
items.append(item)

for l in sugList:
    if l.get('shopinfo'):
    	continue
    	#for ll in l['shopinfo']:
    	#	item = {}
    	#	item['title'] = ll['shopquery']
    	#	url = JDSEARCH + 'keyword=%s' % ll['shopquery']
    	#	item['subtitle'] = u'相关商品数量:' + str(ll['shopcount'])
    	#	item['url'] = url
    	#	item['quickLookURL'] = url
    	#	items.append(item)
    elif l.get('version'):
    	continue
    else:
    	item = {}
    	item['title'] = l['keyword']
    	url = JDSEARCH + 'keyword=%s' % l['keyword']
    	item['subtitle'] = u'相关商品数量:' + str(l['qresult'])
    	item['url'] = url
    	item['quickLookURL'] = url
    	items.append(item)

print json.dumps(items)
