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
if not sys.argv[1:]:
    sys.exit()
keyword = sys.argv[1:]
keyword = "".join(keyword)
query = urllib.urlencode({'wd': keyword})
search_url = 'http://suggestion.baidu.com/su?&zxmode=1&json=1&p=3&sid=&' + query
res = urllib2.Request(search_url)
response = urllib2.urlopen(res)
html = response.read()
response.close()
if not html:
    sys.exit()
html = unicode(html, "gb2312").encode("utf8")
prefix = len("window.baidu.sug(")
# html = html[prefix:]
html = html[prefix:-2]
sugList = json.loads(html)

item['title'] = keyword
item['subtitle'] = "http://www.baidu.com/s?wd=%s" % keyword
item['url'] = "http://www.baidu.com/s?wd=%s" % keyword
item['quickLookURL'] = "http://www.baidu.com/s?wd=%s" % keyword
items.append(item)

for l in sugList['s']:
    item = {}
    item['title'] = l
    url = "http://www.baidu.com/s?wd=%s" % l
    item['subtitle'] = url
    item['url'] = url
    item['quickLookURL'] = url
    items.append(item)
print json.dumps(items)
