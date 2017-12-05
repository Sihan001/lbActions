#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import subprocess
import json
import os
import sys

keyword = "".join(sys.argv[1:])
result = []

rawData = subprocess.check_output(['/Applications/calibre.app/Contents/MacOS/calibredb', 'list', '-f', 'title, cover, formats', '--for-machine'])
rawData = rawData.decode('unicode-escape')
jsonData = json.loads(rawData)


for item in jsonData:

	if item["title"].find(keyword.decode("utf8")) > -1:
	    temp = {}
	    # temp["type"] = "file"
	    _, file_extension = os.path.splitext(item["formats"][0])
	    temp["title"] = "[" + file_extension[1:].upper() + "] " + item["title"]
	    # cover = item["cover"]
	    # itemId = item["id"]
	    # temp["icon"] = "icon.png"
	    temp["subtitle"] = item["formats"][0]
	    temp["path"] = item["formats"][0]
	    result.append(temp)

print json.dumps(result)
