"""
UCSD ECE196 - Posture Protectors
Authors: Abhijit Vadrevu, Aryan Pandhare, Marcus Higashi

Driver for MPU6050 IMU
Reference: https://microcontrollerslab.com/micropython-mpu-6050-esp32-esp8266/
"""

from machine import SoftI2C, Pin


class Imu():
    def __init__(self, scl: int, sda: int, addr=0x68):
        self.i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda))
        self.addr = addr
        self.i2c.start()
        self.i2c.writeto(self.addr, bytearray([107, 0]))
        self.i2c.stop()

    def get_raw_values(self):
        self.i2c.start()
        a = self.i2c.readfrom_mem(self.addr, 0x3B, 14)
        self.i2c.stop()
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["accel_x"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["accel_y"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["accel_z"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["gyro_x"] = self.bytes_toint(raw_ints[8], raw_ints[9])
        vals["gyro_y"] = self.bytes_toint(raw_ints[10], raw_ints[11])
        vals["gyro_z"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        return vals 