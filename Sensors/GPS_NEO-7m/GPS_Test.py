import os

import time
import serial
import adafruit_gps
import requests
import json

uart = serial.Serial("/dev/ttyTHS1", baudrate=9600, timeout=30)
smartBadgeID = 00000
URL = 'http://127.0.0.1:9080/location/'+str(smartBadgeID)+'/' # Your Server IP:Port
headers = {'Content-Type': 'application/json', 'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

gps = adafruit_gps.GPS(uart)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,1000')

last_print = time.monotonic()

while True:

    gps.update()

    current = time.monotonic()
    if current - last_print >= 3.0:
        last_print = current
        if not gps.has_fix:
            print('Waiting for fix...')
            continue
        print('=' * 40)  # Print a separator line.
        print('Latitude: {0:.6f} degrees'.format(gps.latitude))
        print('Longitude: {0:.6f} degrees'.format(gps.longitude))
        data = {
            "smartBadgeID":smartBadgeID,
            "longitude":gps.longitude,
            "latitude":gps.latitude
        }
        r = requests.put(URL, headers=headers, data=json.dumps(data))
