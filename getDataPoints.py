#!/usr/bin/env python3
#
# Command line interface to IntesisHome (AirconWithMe) product on local network
# Tested with Mitsubishi Heavy Industrties (MHI) Air Conditioner unit, but should work with other models as well
# Written by Michiel Tiller (https://github.com/mchlt)
# 

import requests
import json
import urllib3
import os
from IHconstants import *

host='192.168.178.44'
username='operator'
password='operator'

def sendAPIrequest( requestJSON ):
    try: #
        r = requests.post('http://'+host+'/api.cgi', json=requestJSON )
    except err: # Catch any general HTTP errors like 500/400 responces
        print("Connecting to API server failed with error: " + str(err))
        quit(1)
    resp = json.loads(r.text)
    if resp['success'] != True:
        print("Request Failed!")
        print(resp['error'])
        quit(1)
    return(resp)
 

# Login to the API
request={"command":"login","data":{ "username": username, "password": password } }
response=sendAPIrequest( request )
sessionID = response['data']['id']['sessionID']


# Get available data points
request={"command":"getavailabledatapoints","data":{"sessionID":sessionID}}
response=sendAPIrequest( request )
datapoints = response['data']['dp']['datapoints']

# Get all current datapoint values
request={"command":"getdatapointvalue","data":{"sessionID":sessionID,"uid":"all"}}
response=sendAPIrequest( request )
datapointvalues = response['data']['dpval']


for dpv in datapointvalues:
    uid=dpv['uid']
    dp = next((d for d in datapoints if d['uid'] == uid), None)
    if dp['type']==1:
        value = datapointLabels[uid][dpv['value']]
    elif dp['type']==2:
        v = int(dpv['value']/10)
        value = "%2s °C" % v
    else:
        value = dpv['value']
    print("%30s : %s" % (uidString[dpv['uid']], value) )

quit(0)


