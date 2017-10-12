#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import urllib
import os

if not sys.argv[1:]:    
    sys.exit()
keyword = sys.argv[1:]
keyword = "".join(keyword)
query = urllib.urlencode({'wd': keyword})
search_url = 'http://www.baidu.com/s?' + query
os.system("open " + search_url)