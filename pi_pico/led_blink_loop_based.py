"""
Program: LED Blink (loop-based)

Device: Raspberry Pi Pico
Programming Language: MicroPython (save as main.py to run on Pico as default)
Description: Blink the in-built Pico LED via a loop

"""

from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)   # on-board LED - could also define as GPIO-25 -> Pin(25, Pin.OUT)
# or explicitly define the led start state...
# led = Pin("LED", Pin.OUT, value=1)

led.off()

for i in range(0,5):
    print(i)
    led.toggle()
    sleep(0.03)
    led.toggle()
    sleep(0.03)

    # use led.toggle() or...
        # led.value(0)
        # led.value(1)