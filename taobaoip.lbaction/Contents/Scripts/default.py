#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
import json
import urllib, urllib2

# Taobao restful query api
API = 'http://ip.taobao.com/service'

# Regular expression for a valid ip address
REGEXP_IP = r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)'

# i
item = {}
items = []

def query_ip(ip = None):
    '''Query the ip information with the taobao api.'''
    url = '%s/getIpInfo.php?ip=%s' % (API, ip)
    data = None # Get
    req = urllib2.Request(url, data) # exception?
    response = urllib2.urlopen(req)
    html = response.read()
    response.close()
    return json.loads(html)

def generate_feedback_results(ip_query):
    info = query_ip(ip_query)
    if info['code'] == 1:
    	item = {
        	'title': u'查询 IP 地址失败',
            'subtitle': u'错误原因: %s' % info['data'],
            'valid': False
        }
    else:
    	data = info['data']
    	item = {
                'title': u'%s %s %s' % (data['country'], data['region'], data['city']),
                'subtitle': u'运营商: %s %s' % (data['area'], data['isp']),
            }

    items.append(item)
    print json.dumps(items)
            

def main():
    '''The main entry.'''
    # Note: do not use single quote here, because Alfred doesn't give choice to
    # escape a single quote.
    ip_query = "".join(sys.argv[1:])
    generate_feedback_results(ip_query)

if __name__ == '__main__':
    main()
