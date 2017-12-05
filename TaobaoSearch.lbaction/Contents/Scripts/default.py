#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import urllib2
import urllib

SUGURL = 'http://suggest.taobao.com/sug?code=utf-8&'
TAOBAOSEARCH = 'http://s.taobao.com/search?q='

item = {}
items = []

keyword = sys.argv[1:]
keyword = "".join(keyword)
if not keyword:
	sys.exit()

query = urllib.urlencode({'q': keyword})
search_url = SUGURL + query
res = urllib2.Request(search_url)
response = urllib2.urlopen(res)
html = response.read()
response.close()
if not html:
    sys.exit()
sugList = json.loads(html)

item['title'] = keyword
url = TAOBAOSEARCH + keyword
item['subtitle'] = u'淘宝搜索:' + keyword.decode("utf8")
item['url'] = url
item['quickLookURL'] = url
#item['action'] = 't.py'
#item['actionArgument'] = url
#item['actionReturnsItems'] = True
items.append(item)

for l in sugList['result']:
    item = {}
    item['title'] = l[0]
    url = TAOBAOSEARCH + l[0]
    item['subtitle'] = u'相关商品数量:' + str(l[1])
    item['url'] = url
    item['quickLookURL'] = url
    items.append(item)
print json.dumps(items)
