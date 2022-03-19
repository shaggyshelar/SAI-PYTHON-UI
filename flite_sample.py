from ctypes import *
flite_sample = CDLL('./flite_sample.so')


flite_sample.init()
# x = pyflite.select_voice("cmu_us_rms.flitevox")
y = pyflite.text_to_wave("A whole joy was reaping, but they've gone south.")

from array import array
samples = array('h', y['samples'])
with open("SAI From Python.raw", 'wb') as f:
    samples.tofile(f)