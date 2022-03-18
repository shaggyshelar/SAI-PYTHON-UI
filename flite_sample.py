from ctypes import *
adder = CDLL('./flite_sample.so')
adder.start_conversion()