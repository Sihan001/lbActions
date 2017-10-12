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

tmpdir = tempfile.gettempdir()
tqfile = os.path.join(tmpdir, 'tqlocal.txt')
tqlocal = ''
tqurl = 'http://api.map.baidu.com/telematics/v3/weather?output=json&ak=sjiqZ9MndXqeqI4a39TO5IQUf2i2GC7F&'
keyword = sys.argv[1:]
keyword = "".join(keyword)

if keyword:
	with open(tqfile, "w") as fp:
		fp.write(keyword)
else:
	try:
		with open(tqfile, "r") as fp:
			keyword = fp.read()
	except IOError:
			keyword = ''

if not keyword:
	sys.exit()

query = urllib.urlencode({'location': keyword})
tqurl = tqurl + query
res = urllib2.Request(tqurl)
response = urllib2.urlopen(res)
html = response.read()
response.close()
if not html:
    sys.exit()
qtlist = json.loads(html)
if qtlist['error'] != 0:
	sys.exit()

item['title'] = qtlist['results'][0]['currentCity']
item['subtitle'] = "PM2.5: %s" % qtlist['results'][0]['pm25']
item['icon'] = 'icon.png'
items.append(item)

for weather in qtlist['results'][0]['weather_data']:
	item = {}
	item['title'] = weather['date']
	item['subtitle'] = "%s, %s, %s" % (weather['temperature'], weather['wind'], weather['weather'])
	icon = "%s.png" % weather['weather']
	item['icon'] = "%s.png" % weather['weather']
	#if os.path.isfile(icon):
	#	item['icon'] = "%s.png" % weather['weather']
	#else:
	#	item['icon'] = "unknown.png"
	items.append(item)

print json.dumps(items)
