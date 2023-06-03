"""
Sensor Configuration, sets up all sensors and collects data from them
"""

from imu import Imu
from fsr import Fsr
from ultrasonic import UltraSonic

# Sensor Pins
FSR_1_PIN = 34
FSR_2_PIN = 35
FSR_3_PIN = 32

US_TRIG_1_PIN = 33
US_ECHO_1_PIN = 25
US_TRIG_2_PIN = 33
US_ECHO_2_PIN = 25
US_TRIG_3_PIN = 33
US_ECHO_3_PIN = 25
US_TRIG_4_PIN = 33
US_ECHO_4_PIN = 25

IMU_SCL_PIN = 22
IMU_SDA_PIN = 23


class Sensors():
    def __init__(self) -> None:
        self.fsr_1 = Fsr(FSR_1_PIN)
        self.fsr_2 = Fsr(FSR_2_PIN)
        self.fsr_3 = Fsr(FSR_3_PIN)
        self.ultrasonic_1 = UltraSonic(US_TRIG_1_PIN, US_ECHO_1_PIN)
        self.ultrasonic_2 = UltraSonic(US_TRIG_2_PIN, US_ECHO_2_PIN)
        self.ultrasonic_3 = UltraSonic(US_TRIG_3_PIN, US_ECHO_3_PIN)
        self.ultrasonic_4 = UltraSonic(US_TRIG_4_PIN, US_ECHO_4_PIN)
        self.imu = Imu(IMU_SCL_PIN, IMU_SDA_PIN)

    def get_all(self):
        fsr_1 = self.fsr_1.get_raw()
        fsr_2 = self.fsr_2.get_raw()
        fsr_3 = self.fsr_3.get_raw()
        ultrasonic_1 = self.ultrasonic_1.get_distance_cm()
        ultrasonic_2 = self.ultrasonic_2.get_distance_cm()
        ultrasonic_3 = self.ultrasonic_3.get_distance_cm()
        ultrasonic_4 = self.ultrasonic_4.get_distance_cm()
        imu = self.imu.get_values()

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
        return data