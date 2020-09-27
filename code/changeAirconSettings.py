#!/usr/bin/env python3
#
# Command line interface to IntesisHome (AirconWithMe) product on local network
# Tested with Mitsubishi Heavy Industries (MHI) Air Conditioner unit, but should work with other models as well
# Written by Michiel Tiller (https://github.com/mchlt). GPLv3 license.
#
# CLI to set air conditioning parameters
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
        elif power.lower()=='off':
            pwr=0
        else:
            print('Invalid power setting specified')
            printUsage()
            sys.exit(2)
        setdatapointvalue(host, sessionID, UID_ON_OFF, pwr)

    if mode!=None:
        modes=['auto','heat','dry','fan','cool']
        try:
            mde=modes.index(mode.lower())
        except ValueError as e:
            print('Invalid mode specified') 
            printUsage()
            sys.exit(2)
        setdatapointvalue(host, sessionID, UID_USER_MODE, mde)

    if fanspeed!=None:
        try:
            fan=int(fanspeed)
            if (fan<1) or (fan>4):
                raise ValueError
        except:
            print('Invalid fan speed specified')
            printUsage()
            sys.exit(2)
        setdatapointvalue(host, sessionID, UID_FAN_SPEED, fan)
        
    if vanepos!=None:
        if vanepos.lower()=="swing":
            vane=10
        else:
            try:
                vane=int(vanepos)
                if (vane<1) or (vane>4):
                    raise ValueError
            except:
                print('Invalid vane position specified')
                printUsage()
                sys.exit(2)
        setdatapointvalue(host, sessionID, UID_VANE_UP_DOWN_POSITION, vane)

    if temp!=None:
        try:
            tmp=int(temp)
            if (tmp<18) or (tmp>30):
                raise ValueError
        except:
            print('Invalid temperature specified')
            printUsage()
            sys.exit(2)
        tmp=tmp*10
        setdatapointvalue(host, sessionID, UID_USER_SETPOINT, tmp)
 
    logout(host, sessionID)
 

if __name__ == "__main__":
   main(sys.argv[1:])
   sys.exit()

