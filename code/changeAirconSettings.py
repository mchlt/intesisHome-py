#!/usr/bin/env python3
#
# Command line interface to IntesisHome (AirconWithMe) product on local network
# Tested with Mitsubishi Heavy Industrties (MHI) Air Conditioner unit, but should work with other models as well
# Written by Michiel Tiller (https://github.com/mchlt)
#

import os
import sys, getopt
from IHfunctions import *
from IHconstants import *
from configuration import *


def printUsage():
    print('changeAirconSettings.py -s host -p [on|off] -m [auto|heat|dry|fan|cool] -f [1-4] -v [1-4|swing] -t [18-30]')

def main(argv):

    # parse command-line arguments
    host=power=mode=fanspeed=vanepos=temp=None
    try:
        opts, args = getopt.getopt(argv,"hs:p:m:f:v:t:",["host=","power=","mode=","fanspeed=","vanepos=","temp="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printUsage()
            sys.exit()
        elif opt in ("-s", "--host"):
            host = arg
        elif opt in ("-p", "--power"):
            power = arg
        elif opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-f", "--fanspeed"):
            fanspeed = arg
        elif opt in ("-v", "--vanepos"):
            vanepos = arg
        elif opt in ("-t", "--temp"):
            temp = arg

    if host==None:
        print("Error: Host parameter is mandatory.")
        printUsage()
        sys.exit(2)

    # login and get session ID
    sessionID = login(host, username, password)

    if power!=None:
        if power.lower()=='on':
            pwr=1
        else:
            pwr=0
        setdatapointvalue(host, sessionID, 1, pwr)

    if mode!=None:
        modes=['auto','heat','dry','fan','cool']
        try:
            mde=modes.index(mode.lower())
        except ValueError as e:
            print('Invalid mode specified') 
            printUsage()
            sys.exit(2)
        setdatapointvalue(host, sessionID, 2, mde)



if __name__ == "__main__":
   main(sys.argv[1:])
   sys.exit()
