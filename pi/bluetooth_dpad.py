"""
Program: Bluetooth Dpad

Device: Raspberry Pi
Description: Raspberry Pi to respond to dpad buttons pressed on an Android App (via Bluetooth connection).

BlueDot Docs (getting started): https://bluedot.readthedocs.io/en/latest/gettingstarted.html

Packages to Install:
    sudo pip3 install bluedot
"""

from bluedot import BlueDot
from signal import pause

def dpad(pos):
    if pos.top:
        print("up")
    elif pos.bottom:
        print("down")
    elif pos.left:
        print("left")
    elif pos.right:
        print("right")
    elif pos.middle:
        print("fire!")

# Create bluedot object
bd = BlueDot()

# Add listener to dpad buttons on remote
bd.when_pressed = dpad
# bd.when_released = led.off

# Send pause signal to kernel so the program doesn't end - but continues running - hence listening/responing to dpad presses
pause()

