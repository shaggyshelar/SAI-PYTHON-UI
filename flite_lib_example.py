# from ctypes import *
# adder = CDLL('./py_sample.so')
# adder.start_conversion()

import wave
import pygame
import time
import io
import fliteLib

# pygame.mixer.init()
# pygame.mixer.music.set_volume(1.0)

waveOutput = fliteLib.textToWave("hi")
print("**************** Output *********")
print(waveOutput)

# waveBytes = b"".join(waveOutput)
# print(waveBytes)

# bytestreamreader = open('sagar-sai-check.wav','rb')
# print("****************read bytes*********")
# fileReadData = bytestreamreader.read()
# print(fileReadData)
# readBytes = bytearray(fileReadData)
# # print(readBytes)

# # readBytesMemory = bytearray(waveBytes)
# # print(readBytesMemory)


# bytestreamwriter = io.BytesIO()
# temp = io.BytesIO(readBytes)
# pygame.mixer.music.load(temp)
# pygame.mixer.music.play()
# time.sleep(5)