import signal
import RPi.GPIO as GPIO
import sys
import time
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import ST7789

MESSAGE = "READY"
TITLE = "Main Menu"
OPTION1 = "Options"
OPTION2 = "Credits"
OPTION3 = "Configs"

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

cwd = "{}/SAI-PYTHON-UI/".format(os.getcwd())
cwd1 = os.getcwd()

print("{}/Flite/test.wav".format(cwd))
subprocess.run(['aplay',"{}/Flite/test.wav".format(cwd1)])

# The buttons on Pirate Audio are connected to pins 5, 6, 16 and 24
# Boards prior to 23 January 2020 used 5, 6, 16 and 20
# try changing 24 to 20 if your Y button doesn't work.
BUTTONS = [5, 6, 16, 24]

# These correspond to buttons A, B, X and Y respectively
LABELS = ['A', 'B', 'X', 'Y']

# Set up RPi.GPIO with the "BCM" numbering scheme
GPIO.setmode(GPIO.BCM)

# Buttons connect to ground when pressed, so we should set them up
# with a "PULL UP", which weakly pulls the input signal to 3.3V.
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# "handle_button" will be called every time a button is pressed
# It receives one argument: the associated input pin.
def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    global MESSAGE
    MESSAGE  = "Button: {}".format(label)
    # sound = AudioSegment.from_wav("{}/Flite/{}.wav".format(cwd,label))
    # play(sound)
    print("{}/Flite/{}.wav".format(cwd,label))
    subprocess.run(['aplay',"{}/Flite/{}.wav".format(cwd1,label)])
    print("Button press detected on pin: {} label: {}".format(pin, label))


# Loop through out buttons and attach the "handle_button" function to each
# We're watching the "FALLING" edge (transition from 3.3V to Ground) and
# picking a generous bouncetime of 100ms to smooth out button presses.
for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=100)

disp.begin()

WIDTH = disp.width
HEIGHT = disp.height


img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

title_size_x, title_size_y = draw.textsize(TITLE, font)
title_text_x = (disp.width - title_size_x) // 2

option1_size_x, option1_size_y = draw.textsize(OPTION1, font)
option1_text_x = (disp.width - option1_size_x) // 2
option1_text_y = title_size_y


option2_size_x, option2_size_y = draw.textsize(OPTION2, font)
option2_text_x = (disp.width - option2_size_x) // 2
option2_text_y = title_size_y * 2


option3_size_x, option3_size_y = draw.textsize(OPTION3, font)
option3_text_x = (disp.width - option3_size_x) // 2
option3_text_y = title_size_y * 3

size_x, size_y = draw.textsize(MESSAGE, font)
text_x = disp.width
text_y = size_y * 4

t_start = time.time()
while True:
    x = (time.time() - t_start) * 100
    x %= (size_x + disp.width)
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((int(title_text_x), 0), TITLE, font=font, fill=(255, 255, 255))
    draw.text((int(option1_text_x), option1_text_y), OPTION1, font=font, fill=(255, 255, 255))
    draw.text((int(option2_text_x), option2_text_y), OPTION2, font=font, fill=(255, 255, 255))
    draw.text((int(option3_text_x), option3_text_y), OPTION3, font=font, fill=(255, 255, 255))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)

# Finally, since button handlers don't require a "while True" loop,
# we pause the script to prevent it exiting immediately.
# signal.pause()
