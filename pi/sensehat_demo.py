"""
Program: SenseHat Demo

Device: Raspberry Pi
Description: Demo of some of the functions of a SenseHat

SenseHat Docs: https://pythonhosted.org/sense-hat/api/

Packages to Install:
    sudo apt-get install sense-hat

"""

from sense_hat import SenseHat

sense = SenseHat()

# Flip sensehat vertical orientation
# sense.flip_v()


# Flip sensehat horizontal orientation
# sense.flip_h()


# sense.show_message("Hello world!")

# [QUESTION MARK]

X = [255, 0, 0]         # Red
O = [255, 255, 255]     # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)

"""
# Clear
sense.clear()       # no arguments defaults to off
sense.clear(red)    # passing in an RGB tuple

# Load Image
sense.load_image("space_invader.png")

# Scroll text across
sense.show_message("One small step for Pi!", text_colour=[255, 0, 0],scroll_speed=0.1)

# Low Light mode
sense.low_light = True

# Get humidity
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)
# or...
print(sense.humidity)

# Get Temp
temp = sense.get_temperature()
print("Temperature: %s C" % temp)
# alternatives
print(sense.temp)
print(sense.temperature)

# Get orientation
orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# Get orientation from Gyroscope
gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
# alternatives
print(sense.gyro)
print(sense.gyroscope)

"""


