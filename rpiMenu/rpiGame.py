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

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # self.main_menu = MainMenu(self)
        # self.options = OptionsMenu(self)
        # self.credits = CreditsMenu(self)
        # self.curr_menu = self.main_menu
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
        for pin in self.BUTTONS:
            GPIO.add_event_detect(pin, GPIO.FALLING, self.handle_button, bouncetime=100)
    
    def handle_button(self, pin):
        label = self.LABELS[self.BUTTONS.index(pin)]
        print("Button press detected on pin: {} label: {}".format(pin, label))
        
    def game_loop(self):
        while self.playing:
            x = (time.time() - self.t_start) * 100
            x %= (self.title_size_x + self.disp.width)
            self.draw.rectangle((0, 0, self.disp.width, self.disp.height), (0, 0, 0))
            self.draw.text((int(self.title_text_x), 0), self.TITLE, font=self.font, fill=(255, 255, 255))
            self.disp.display(self.img)
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        pass
        # font = pygame.font.Font(self.font_name,size)
        # text_surface = font.render(text, True, self.WHITE)
        # text_rect = text_surface.get_rect()
        # text_rect.center = (x,y)
        # self.display.blit(text_surface,text_rect)