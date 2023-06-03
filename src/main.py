import json
import utime
from sensor_config import Sensors
from bluetooth import BLEUART
import ubluetooth

REFRESH_RATE_HZ = 1
REFRESH_PERIOD_MS = 1000 // REFRESH_RATE_HZ

sensors = Sensors()
ble = ubluetooth.BLE()
uart = BLEUART(ble)



def main():
    start_time = utime.ticks_ms()
    while True:
        loop_time = utime.ticks_ms()
        if utime.ticks_diff(loop_time, start_time) > REFRESH_PERIOD_MS:
            print('Getting sensor data')
            raw_data = sensors.get_all()
            data = json.dumps(raw_data)
            print(f'Data: {data}')
            print('Sending sensor data')
            uart.write(data)
            start_time = loop_time


main()