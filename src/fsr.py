"""
UCSD ECE196 - Posture Protectors
Authors: Abhijit Vadrevu, Aryan Pandhare, Marcus Higashi

Driver for Force Sensitive Resistor
Reference: https://docs.micropython.org/en/latest/esp8266/tutorial/adc.html
"""

from machine import ADC, Pin


class Fsr():
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)
        self.adc = ADC(self.pin)
        self.adc.atten(ADC.ATTN_11DB)

    def get_raw(self) -> int:
        return self.adc.read_u16()
    
    def get_voltage(self) -> int:
        return self.adc.read_uv()