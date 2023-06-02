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
IMU_SDA_PIN = 21

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
