# IntesisHome (AirconWithMe) interface strings
# Written by Michiel Tiller (https://github.com/mchlt)
# 

UID_ON_OFF = 1
UID_USER_MODE = 2
UID_FAN_SPEED = 4
UID_VANE_UP_DOWN_POSITION = 5
UID_USER_SETPOINT = 9
UID_RETURN_PATH_TEMPERATURE = 10
UID_REMOTE_DISABLE = 12
UID_ON_TIME = 13
UID_ALARM_STATUS = 14
UID_ERROR_CODE = 15
UID_MIN_TEMPERATURE_SETPOINT = 35
UID_MAX_TEMPERATURE_SETPOINT = 36
UID_OUTDOOR_TEMPERATURE = 37
UID_MAINTENANCE_TIME = 181
UID_MAINTENANCE_CONFIG = 182
UID_MAINTENANCE_FILTER_TIME = 183
UID_MAINTENANCE_FILTER_CONFIG = 184

uidLabels={
    1:"On/off",
    2:"User Mode",
    4:"Fan Speed",
    5:"Vane Up/Down position",
    9:"User Setpoint",
    10:"Return Path Temperature",
    12:"Remote Disable",
    13:"On Time",
    14:"Alarm Status",
    15:"Error Code",
    35:"Min Temperature Setpoint",
    36:"Max Temperature Setpoint",
    37:"Outdoor Temperature",
    181:"Maintenance time",
    182:"Maintenance config",
    183:"Maintenance Filter time",
    184:"Maintenance Filter config"
}

datapointLabels = {
 1:  {0:'Off',1:'On'}, 
 2:  {0:'Auto', 1:'Heat', 2:'Dry', 3:'Fan', 4:'Cool'},
 4:  {1:'Speed 1', 2:'Speed 2', 3:'Speed 3', 4:'Speed 4'},
 5:  {1:'Position 1', 2:'Position 2', 3:'Position 3', 4:'Position 4', 10:'Swing'},
 12: {0:'Remote Enabled',1:'Remote Disabled'}, 
 14: {0:'Off',1:'On'}
}

