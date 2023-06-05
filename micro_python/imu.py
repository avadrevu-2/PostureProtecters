from machine import I2C
from machine import Pin
from machine import sleep
import mpu6050


i2c = I2C(scl=Pin(22), sda=Pin(23))     #initializing the I2C method for ESP32
mpu= mpu6050.accel(i2c)
while True:
    mpu.get_values()
    print(mpu.get_values())
    sleep(500)
