# intesisHome-py
Python library to manage intesisHome (AirconWithMe) wifi interfaces commonly found in domestic air conditioner appliances
I have Mistubishi Heavy Industries (MHI) air conditioner units with the AirconWithMe wifi interface, with which I tested this to work. 

getDataPoints.py is a simple tool made for testing thats connect to the IntesisHome interface and returns all data points the interface knows. 
Example output:
```
$ python3 getDataPoints.py
                        On/off : Off
                     User Mode : Dry
                     Fan Speed : Speed 1
         Vane Up/Down position : Position 1
                 User Setpoint : 21 °C
       Return Path Temperature : 22 °C
                Remote Disable : Remote Enabled
                       On Time : 0
                  Alarm Status : Off
                    Error Code : 0
      Min Temperature Setpoint : 18 °C
      Max Temperature Setpoint : 30 °C
           Outdoor Temperature : 18 °C
              Maintenance time : 0
            Maintenance config : 0
       Maintenance Filter time : 0
     Maintenance Filter config : 0
```
