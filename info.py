# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Copyright (c) 2017 Adafruit Industries
# Author: Ladyada, Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

# Import Python System Libraries
import json
import subprocess
import time

# Import Requests Library
import requests

# Import Blinka
from board import SCL, SDA
import busio
import adafruit_ssd1306

# Import Python Imaging Library
from PIL import Image, ImageDraw, ImageFont

API_TOKEN = "YOUR_API_TOKEN_HERE"
api_url = "http://localhost/admin/api.php?summaryRaw&auth="+API_TOKEN

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Leaving the OLED on for a long period of time can damage it

# Leaving the OLED on for a long period of time can damage it
# Set these to prevent OLED burn in
DISPLAY_ON  = 10 # on time in seconds
DISPLAY_OFF = 50 # off time in seconds

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position
# for drawing shapes.
x = 0

# Load nice silkscreen font
font = ImageFont.truetype('/home/expire/slkscr.ttf', 18)
speed = 0.2


# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+8),     str("F    "), font=font, fill=200)
disp.image(image)
disp.show()
time.sleep(speed)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+8),     str(" E   "), font=font, fill=200)
disp.image(image)
disp.show()
time.sleep(speed)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+8),     str("  L  "), font=font, fill=200)
disp.image(image)
disp.show()
time.sleep(speed)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+8),     str("   I "), font=font, fill=200)
disp.image(image)
disp.show()
time.sleep(speed)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+8),     str("    X"), font=font, fill=200)
disp.image(image)
disp.show()
time.sleep(speed)

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+8),     str("FELIX"), font=font, fill=200)
disp.image(image)
disp.show()
time.sleep(5)

disp.fill(0)
disp.show()
#     cmd = "top -bn1 | grep load | awk " \
#           "'{printf \"CPU Load: %.2f\", $(NF-2)}'"
#     CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")

#     # skip over original stats
#     draw.text((x, top+8),     str("FELIX"), font=font, fill=200)
#     draw.text((x, top+19),    str(CPU),  font=font, fill=255)
#    # draw.text((x, top+25),    str(Disk),  font=font, fill=255)

    # # Display image.
    # disp.image(image)
    # disp.show()
    # time.sleep(DISPLAY_ON)
    # disp.fill(0)
    # disp.show()
    # time.sleep(DISPLAY_OFF)
