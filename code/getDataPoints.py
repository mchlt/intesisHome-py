#!/usr/bin/env python3
#
# Command line interface to IntesisHome (AirconWithMe) product on local network
# Tested with Mitsubishi Heavy Industrties (MHI) Air Conditioner unit, but should work with other models as well
# Written by Michiel Tiller (https://github.com/mchlt)
# 

import os
from IHfunctions import *
from IHconstants import *
from configuration import *

host='aircoslaapkamer'

# login and get session ID
sessionID = login(host, username, password)

# Get available data points
datapoints = getavailabledatapoints(host, sessionID)

# Get all current datapoint values
datapointvalues = getdatapointvalue(host, sessionID)


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

logout(host, sessionID)

sys.exit()


