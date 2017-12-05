#!/usr/bin/env python
# -*- coding:utf-8 -*-
# LaunchBar Action Script
import sys
import math
import json

def numtoCny(num):     
	capUnit = ['万','亿','万','圆','']     
	capDigit = { 2:['角','分',''], 4:['仟','佰','拾','']}     
	capNum=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']     
	snum = str('%019.02f') % num     
	if snum.index('.')>16:     
		return ''    
	ret,nodeNum,subret,subChr='','','',''    
	CurChr=['','']     
	for i in range(5):     
		j=int(i*4+math.floor(i/4))     
		subret=''    
		nodeNum=snum[j:j+4]     
		lens=len(nodeNum)     
		for k in range(lens):     
			if int(nodeNum[k:])==0:     
				continue    
			CurChr[k%2] = capNum[int(nodeNum[k:k+1])]     
			if nodeNum[k:k+1] != '0':     
				CurChr[k%2] += capDigit[lens][k]     
			if  not ((CurChr[0]==CurChr[1]) and (CurChr[0]==capNum[0])):     
				if not((CurChr[k%2] == capNum[0]) and (subret=='') and (ret=='')):     
					subret += CurChr[k%2]     
		subChr = [subret,subret+capUnit[i]][subret!='']     
		if not ((subChr == capNum[0]) and (ret=='')):     
			ret += subChr     
	return [ret,capNum[0]+capUnit[3]][ret=='']  

def callback(strs):
	item = {}
	items = []
	item['title'] = strs
	item['action'] = 'r.py'
	item['actionArgument'] = strs
	item['actionReturnsItems'] = True
	items.append(item)
	print json.dumps(items)

callback(numtoCny(float("".join(sys.argv[1:]))))

