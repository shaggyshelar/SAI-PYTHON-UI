#!/usr/bin/env python3
from ctypes import *
import RPi.GPIO as GPIO
import time
import os
import pygame
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pygame import mixer
import io
import ST7789
adder = CDLL('./adder.so')

MESSAGE = "READY"
TITLE = "Main Menu"
OPTION1 = "Options"
OPTION2 = "Credits"
OPTION3 = "Configs"

res_int = adder.add_int(4,5)
print("Sum of 4 and 5 = {}".format(res_int))

res_int1 = adder.add_new(3,2)
print("Sum of 3 and 2 = {}".format(res_int1))

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

# print("{}/Flite/test.wav".format(cwd))
mixer.init()

mixer.music.load("Flite/test.wav")
mixer.music.set_volume(0.7)
mixer.music.play()

# In Memory bytes to pymixer play
# bytestreamreader = open('pythonGeneratedWav.wav','rb')
# readBytes = bytearray(bytestreamreader.read())
# bytestreamwriter = io.BytesIO()
# temp = io.BytesIO(readBytes)
# pygame.mixer.music.load(temp)
# pygame.mixer.music.play()
# time.sleep(5)

a_sound = pygame.mixer.Sound("Flite/A.wav")
b_sound = pygame.mixer.Sound("Flite/B.wav")
x_sound = pygame.mixer.Sound("Flite/X.wav")
y_sound = pygame.mixer.Sound("Flite/Y.wav")

BUTTONS = [5, 6, 16, 24]
LABELS = ['A', 'B', 'X', 'Y']
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    global MESSAGE
    MESSAGE  = "Button: {}".format(label)
    pygame.mixer.stop()
    if label == "A":
        a_sound.play()
    elif label == "B":
        b_sound.play()
    elif label == "X":
        x_sound.play()
    elif label == "Y":
        y_sound.play()
    print("Button press detected on pin: {} label: {}".format(pin, label))

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

# signal.pause()
