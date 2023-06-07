"""
UCSD ECE196 - Posture Protectors
Authors: Abhijit Vadrevu, Aryan Pandhare, Marcus Higashi

Main script for the ESP32. 
Collects data from sensors and sends it over BLE.
"""


import json
import ubluetooth
from machine import Timer
from sensor_config import Sensors
from ble_uart import BLEUART

REFRESH_RATE_HZ = 1
REFRESH_PERIOD_MS = 1000 // REFRESH_RATE_HZ

sensors = Sensors()
ble = ubluetooth.BLE()
uart = BLEUART(ble)



def main(timer: Timer):
    print('Getting sensor data')
    raw_data = sensors.get_all()
    data = json.dumps(raw_data)
    print(f'Data: {data}')
    print('Sending sensor data')
    uart.write(data)


timer = Timer(0)
timer.init(period=REFRESH_PERIOD_MS, mode=Timer.PERIODIC, callback=main)
