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
from rpiMenu import *
import ST7789
from rpiMenu import MainMenu

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.DISPLAY_W, self.DISPLAY_H = 240, 240
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.BUTTONS = [5, 6, 16, 24]
        self.LABELS = ['A', 'B', 'X', 'Y']
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.img = Image.new('RGB', (240, 240), color=(0, 0, 0))
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
        self.t_start = time.time()
        self.TITLE = "Main Menu"
        self.disp = ST7789.ST7789(
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
        self.title_size_x, self.title_size_y = self.draw.textsize(self.TITLE, self.font)
        self.title_text_x = (self.disp.width - self.title_size_x) // 2
        mixer.init()
        self.disp.begin()
        print("display begin")
        for pin in self.BUTTONS:
            GPIO.add_event_detect(pin, GPIO.FALLING, self.handle_button, bouncetime=100)
    
    def handle_button(self, pin):
        label = self.LABELS[self.BUTTONS.index(pin)]
        print("Button press detected on pin: {} label: {}".format(pin, label))
        
    def game_loop(self):
        while self.playing:
            self.draw.rectangle((0, 0, self.disp.width, self.disp.height), (0, 0, 0))
            self.draw_text("Thanks for playing", self.title_text_x, 0)
            # self.draw_text("Options", self.title_text_x, self.title_size_y)
            # self.draw_text("*", 0, self.title_size_y )
            # self.draw_text("Credits", self.title_text_x, self.title_size_y * 2)
            # self.draw_text("Configs", self.title_text_x, self.title_size_y * 3)
            self.disp.display(self.img)
            self.reset_keys()

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, x, y ):
        self.draw.text((x, y), text, font=self.font, fill=(255, 255, 255))
