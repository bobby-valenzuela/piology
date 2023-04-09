"""
Program: Motion Dtection with servo motor

Device: Raspberry Pi Pico
Programming Language: MicroPython (save as main.py to run on Pico as default)
Description: IR Motion sensor on Pico detects movement and a connected Servo motor rotates (and onboard-LED lights up).

"""

from utime import sleep
from machine import Pin, PWM

# IR Sensor [GPIO-0]
prox_sensor = Pin(0, Pin.IN)

# Servo motor [GPIO-1]
servo_01 = PWM(Pin(1))
# Frequency in HZ
servo_01.freq(50)

# Servo Config
MIN = 1000000
MIN = 1500000
MAX = 2000000

# Onboard led
led = Pin("LED",Pin.OUT)

def detected_obj():
    # prox_sensor.value() == 0 : means something IS detected 
    return 1 if prox_sensor.value() == 0 else 0

def move_servo(dir):

    if dir == 'l':
        servo_01.duty_ns(MAX)
    else:
        servo_01.duty_ns(MIN)

# Initiate: servo left by default
move_servo('l')

while True:

    print(detected_obj())

    if detected_obj() == 0 :
        led.off()
        move_servo('l')
    else:
        led.on()
        move_servo('r')

    sleep(0.15)
