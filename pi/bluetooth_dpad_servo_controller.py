#!/usr/bin/env python

"""
Program: Bluetooth dpad servo controller

Device: Raspberry Pi
Programming Language: MicroPython (save as main.py to run on Pico as default)
Description: Dpad on Android app to control with servo motor on Pi via Bluetooth

BlueDot Docs (getting started): https://bluedot.readthedocs.io/en/latest/gettingstarted.html

Packages to Install:
    sudo pip3 install bluedot

"""

print("Running...")

from gpiozero import AngularServo, Device
from time import sleep
from bluedot import BlueDot
from signal import pause

# Prevent jitter by changing pin factory
from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()

# pause()


# Initialize Servo Instance
# Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19

# servo = Servo(13) -> Using servo module
servo = AngularServo(13, min_angle=44, max_angle=-42)
servo.angle = 0.0

# Create bluedot object
bd = BlueDot()

def dpad(pos):
    
    if pos.top:
        print("up")
        left_right(0.3)

    elif pos.bottom:
        print("down")
        left_right(0.2,4)

    elif pos.left:
        print("left")
        servo.angle = -42

    elif pos.right:
        print("right")
        servo.angle = 44

    elif pos.middle:
        print("middle")
        servo.angle = 0.0

def left_right(naptime, step = 1):
    
    for deg in range(-42,44, step):
        
        if deg > 44:
            break

        servo.angle = deg
        sleep(naptime)


# Add listener to dpad buttons on remote
bd.when_pressed = dpad
# bd.when_released = led.off

# Send pause signal to kernel so the program doesn't end - but continues running - hence listening/responing to dpad presses
pause()
