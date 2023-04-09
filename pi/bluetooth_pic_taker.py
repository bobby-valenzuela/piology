"""
Program: Bluetooth Pic Taker

Device: Raspberry Pi
Description: Use Android App to control your Pi via Bluetooth and take a picture via a raspicam connected to your Pi.

BlueDot Docs (getting started): https://bluedot.readthedocs.io/en/latest/gettingstarted.html
Libcamera: https://www.raspberrypi.com/documentation/computers/camera_software.html#libcamera-and-libcamera-apps

Packages to Install:
    sudo pip3 install bluedot

"""

from bluedot import BlueDot
import os

bd = BlueDot()
num = 0

while True:

    bd.wait_for_press()
    print("You pressed the blue dot!")
    
    # Take pic and save to 'img<num>.jpg'
    os.system("libcamera-jpeg -o img" + str(num) + ".jpg")
    num+= 1