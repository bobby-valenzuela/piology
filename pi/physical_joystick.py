#!/usr/bin/env python
"""
Program: GPIO Joystick

Device: Raspberry Pi
Description: Respond to joystick movement

"""
from gpiozero import Button
from time import sleep
from subprocess import check_call

# Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19

# Press in joystick [GPIO-24]
button = Button(24)

# X-axis [GPIO-18]
joystick_x = Button(18)
# Y-axis [GPIO-19]
joystick_y = Button(19)


while True:
    
    if button.is_pressed:
        print("Btn Pressed")

    # if button.when_released:


    if joystick_x.is_pressed:
        value = joystick_x.value()
        print("Going X... " + str(value))

    if joystick_y.is_pressed:
        value = joystick_y.value()
        print("Going Y... " + str(value))



# [OPTIONAL] Shutdown button
# def shutdown():
#     check_call(['sudo', 'poweroff'])

# shutdown_btn = Button(18, hold_time=2)
# shutdown_btn.when_held = shutdown

# pause()