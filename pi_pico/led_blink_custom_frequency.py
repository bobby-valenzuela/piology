"""
Program: LED Blink with custom frequency

Device: Raspberry Pi Pico
Programming Language: MicroPython (save as main.py to run on Pico as default)
Description: Blink the in-built Pico LED with a manually defined frequency.

"""

from machine import Pin, Timer

led = Pin("LED", Pin.OUT) # on-board LED - could also define as GPIO-25 -> Pin(25, Pin.OUT)
timer = Timer()

def ledblink(timer):

    led.toggle()

# From docs on Timer https://docs.micropython.org/en/latest/library/machine.Timer.html
    # freq - The timer frequency, in units of Hz. The upper bound of the frequency is dependent on the port. When both the freq and period arguments are given, freq has a higher priority and period is ignored.
    # period - The timer period, in milliseconds.
    # Timer.PERIODIC - The timer runs periodically at the configured frequency of the
    # callback - The callable to call upon expiration of the timer period. The callback must take one argument, which is passed the Timer object.

# Frequency-based
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=ledblink)


# Millisecond-based (100ms)
# timer.init(period=100, callback=ledblink)