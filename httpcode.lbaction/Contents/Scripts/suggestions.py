#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
#import json

#items = []

# Note: The first argument is the script path!
#for i in range(1, len(sys.argv)):
#    argument = sys.argv[i]
#    item = {}
#    item['title'] = argument
#    items.append(item)
#    item = {}
#    item['title'] = argument + argument
#    items.append(item)
#
#print json.dumps(items)

'''
HTTP Status Code v0.1

Github: https://github.com/ilstar/http_status_code
Author: Fred Liang
'''

import csv

from feedback import Feedback

query = "".join(sys.argv[1:])
query = query.lower()
baseurl = 'http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#'

fb = Feedback()

with open('status_code.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        code, desc = row
        lower_desc = desc.lower()

        if code.find(query) != -1:
            fb.add_item(desc, code, arg=baseurl + code)
        elif lower_desc.find(query) != -1:
            fb.add_item(code, desc, arg=baseurl + code)

print fb
