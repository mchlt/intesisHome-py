# IHfunctions.py
#
#
#   Copyright (C) 2020 Michiel Tiller
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
import json
import sys

def sendAPIrequest(host, requestJSON):
    try: #
        r = requests.post('http://'+host+'/api.cgi', json=requestJSON )
    except err: # Catch any general HTTP errors like 500/400 responces
        print("Connecting to API server failed with error: " + str(err))
        sys.exit(1)
    resp = json.loads(r.text)
    if resp['success'] != True:
        print("Request Failed!")
        print(resp['error'])
        sys.exit(1)
    return(resp)

def login(host, username, password):
    request={"command":"login","data":{ "username": username, "password": password }}
    response=sendAPIrequest(host, request)
    return(response['data']['id']['sessionID'])

def logout(host, sessionID):
    request={"command":"logout","data":{"sessionID":sessionID}}
    response=sendAPIrequest(host, request)
    return(response['success'])
	
def getavailabledatapoints(host, sessionID):
    request={"command":"getavailabledatapoints","data":{"sessionID":sessionID}}
    response=sendAPIrequest(host, request)
    return(response['data']['dp']['datapoints'])

def getdatapointvalue(host, sessionID, uid="all"):
    request={"command":"getdatapointvalue","data":{"sessionID":sessionID,"uid":uid}}
    response=sendAPIrequest(host, request)
    return(response['data']['dpval'])

def setdatapointvalue(host, sessionID, uid, value):
    request={"command":"setdatapointvalue","data":{"sessionID":sessionID,"uid":uid,"value":value}}
    response=sendAPIrequest(host, request)
    return(response['success'])

