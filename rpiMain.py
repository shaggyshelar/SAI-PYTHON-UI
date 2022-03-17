import signal
import RPi.GPIO as GPIO
import sys
import time
from rpiMenu import *

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789


from rpiGame import Game
g = Game()

MESSAGE = "READY"

disp = ST7789.ST7789(
        height=240,
        width=240,
        rotation=90,
        port=0,
        cs=1,
        dc=9,
        backlight=13,
        spi_speed_hz=60 * 1000 * 1000,
        offset_left=0,
        offset_top=0
   )


print("""buttons.py - Detect which button has been pressed
This example should demonstrate how to:
1. set up RPi.GPIO to read buttons,
2. determine which button has been pressed
Press Ctrl+C to exit!
""")

BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    global MESSAGE
    MESSAGE  = "Button: {}".format(label)
    print("Button press detected on pin: {} label: {}".format(pin, label))
for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=100)

disp.begin()

WIDTH = disp.width
HEIGHT = disp.height
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
size_x, size_y = draw.textsize(MESSAGE, font)
text_x = disp.width
text_y = (disp.height - size_y) // 2
t_start = time.time()
# x = size_x + disp.width
while True:
    x = 200
    x %= (size_x + disp.width)
#    x = size_x + disp.width
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)

# Finally, since button handlers don't require a "while True" loop,
# we pause the script to prevent it exiting immediately.
# signal.pause()