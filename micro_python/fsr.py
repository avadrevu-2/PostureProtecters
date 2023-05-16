from machine import ADC, Pin
import time


pin = Pin(0)

adc = ADC(pin)
val = adc.read_uv()

while True:
    val = adc.read_uv()
    print(val)
    time.sleep(0.2)

