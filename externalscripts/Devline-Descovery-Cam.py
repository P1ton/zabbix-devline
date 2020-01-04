#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import requests, xmltodict, json, re
from sys import argv

script, lineHost, linePort, lineUser, linePassword = argv

uri = 'http://' + lineHost + ':' + linePort + '/cameras'
req = requests.get(uri, auth=(lineUser, linePassword))
xml = xmltodict.parse(req.text)
json = json.dumps(xml)

json = json.replace('"camera-list": {', '')
json = json.replace('"camera":', '"data":')

json = json.replace('"uri":', '"{#CAMURI}":')
json = json.replace('"name":', '"{#CAMNAME}":')
json = json.replace('"width":', '"{#CAMWIDTH}":')
json = json.replace('"height":', '"{#CAMHEIGHT}":')
json = json.replace('"pixel-aspect-ratio-x":', '"{#CAMPIXASRX}":')
json = json.replace('"pixel-aspect-ratio-y":', '"{#CAMPIXASRY}":')
json = json.replace('"image-uri":', '"{#CAMIMAGEURI}":')
json = json.replace('"video-uri":', '"{#CAMVIDEOURI}":')
json = json.replace('"streaming-uri":', '"{#CAMSTREAMURI}":')
json = json.replace('"osd-uri":', '"{#CAMOSDURI}":')

json = json[:-1]

print(json)
