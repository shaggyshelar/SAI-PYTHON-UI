from distutils.core import setup, Extension
import os

inc_dirs=['./include']

# For M1 Mac OS
# lib_dirs=['./flite/build/x86_64-darwin21.1.0/lib']

# For Raspberry Pi Zero W V1
lib_dirs=['./build/armv6l-linux-gnueabihf/lib']
#lib_dirs=['./build/armv6l-linux-gnueabihf/lib','/usr/local/lib/python3.9','/usr/include/alsa']

setup(name = 'fliteLib', version = '1.0',  \
   ext_modules = [Extension('fliteLib', ['flite_lib.c'],
                             include_dirs=inc_dirs,
                             library_dirs=lib_dirs,
                             libraries=['asound', 'flite_cmu_us_kal', 'flite_usenglish', 'flite_cmulex', 'flite', 'm'])]
)