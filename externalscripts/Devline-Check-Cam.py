#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import requests
from sys import argv

script, camName, camImg, lineHost, linePort, lineUser, linePassword = argv

uri = 'http://' + lineHost + ':' + linePort + camImg

try:
	req = requests.get(uri, auth=(lineUser, linePassword))
	if req.status_code == 200:
		print('1')
	else:
		print('0')
except:
	print('0')
