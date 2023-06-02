import json
from machine import Timer
from sensor_config import Sensors
from bluetooth import BLE


REFRESH_RATE_HZ = 2
REFRESH_PERIOD_MS = 1000 // REFRESH_RATE_HZ

sensors = Sensors()
ble = BLE('ESP32')


def main():
    print('Getting sensor data')
    fsr_1 = sensors.fsr_1.get_raw()
    fsr_2 = sensors.fsr_2.get_raw()
    fsr_3 = sensors.fsr_3.get_raw()
    ultrasonic_1 = sensors.ultrasonic_1.get_distance_cm()
    ultrasonic_2 = sensors.ultrasonic_2.get_distance_cm()
    ultrasonic_3 = sensors.ultrasonic_3.get_distance_cm()
    ultrasonic_4 = sensors.ultrasonic_4.get_distance_cm()
    imu = sensors.imu.get_values()

    # Format sensor data
    data = {
        'fsr_1': fsr_1,
        'fsr_2': fsr_2,
        'fsr_3': fsr_3,
        'ultrasonic_1': ultrasonic_1,
        'ultrasonic_2': ultrasonic_2,
        'ultrasonic_3': ultrasonic_3,
        'ultrasonic_4': ultrasonic_4,
        'accel_x': imu['accel_x'],
        'accel_y': imu['accel_y'],
        'accel_z': imu['accel_z'],
        'gyro_x': imu['gyro_x'],
        'gyro_y': imu['gyro_y'],
        'gyro_z': imu['gyro_z']
    }
    data = json.dumps(data)
    print(f'Data: {data}')

    print('Sending sensor data')
    ble.send(data)


# Create timer to run main() at REFRESH_RATE_HZ
timer = Timer()
timer.init(period=REFRESH_PERIOD_MS, mode=Timer.PERIODIC, callback=main)
