# IHfunctions.py
# Written by Michiel Tiller (https://github.com/mchlt). GPLv3 license
#

import requests
import json

def sendAPIrequest(host, requestJSON):
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

def login(host, username, password):
    request={"command":"login","data":{ "username": username, "password": password }}
    response=sendAPIrequest(host, request)
    return(response['data']['id']['sessionID'])
	
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

