#!/usr/bin/python

import os
import requests
import commands
import datetime
import json
import time

url="http://api.yeelink.net/v1.0/device/355027/sensor/401458/datapoints"
apiheaders={'U-ApiKey':'62f04b4ea8bb877e1a84ab127b850dd3','content-type': 'application/json'}

while True:
	now = datetime.datetime.now()
	(status, temp) = commands.getstatusoutput('python ds18b20.py')
	info={
		'timestamp' : now.strftime('%Y-%m-%dT%H:%M:%S'),
		'value' : temp
		}
	
	print info
	r=requests.post(url, headers=apiheaders, data=json.dumps(info))
	print r
	print "sleep for 20 sec..."
	time.sleep(20)
