"""
UCSD ECE196 - Posture Protectors
Authors: Abhijit Vadrevu, Aryan Pandhare, Marcus Higashi

Driver for HC-SR04 Ultrasonic Sensor
Reference: https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py
"""

from machine import Pin, time_pulse_us
from utime import sleep_us


class UltraSonic():
    def __init__(self, trig: int, echo: int, timeout_us=30000):
        self.timeout_us = timeout_us
        self.trig = Pin(trig, Pin.OUT)
        self.echo = Pin(echo, Pin.IN, pull=Pin.PULL_DOWN)
        self.trig.value(0)


    def send_pulse_and_time(self) -> int:
        # Stabalize value at 0
        self.trig.value(0)
        sleep_us(5)

        # Send a 5us pulse.
        self.trig.value(1)
        sleep_us(10)
        self.trig.value(0)

        # Wait 'timeout_us' microseconds for the echo pin to go high
        try:
            pulse_time = time_pulse_us(self.echo, 1)
            print(pulse_time)
            if pulse_time < 0:  # If we timed out, then return -1
                return -1
            return pulse_time
        except Exception as e:
            print("Exception: ", e)
            return -1           

    def get_distance_cm(self) -> float:
        pulse_time = self.send_pulse_and_time()
        if pulse_time < 0:
            return -1
        distance_cm = (pulse_time / 2) / 29.1
        return distance_cm
