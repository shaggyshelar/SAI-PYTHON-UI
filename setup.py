from distutils.core import setup, Extension
import os

inc_dirs=['./flite/include']

# For M1 Mac OS
# lib_dirs=['./flite/build/x86_64-darwin21.1.0/lib']

# For Raspberry Pi Zero W V1
lib_dirs=['./flite/build/armv6l-linux-gnueabihf/lib']

setup(name = 'fliteLib', version = '1.0',  \
   ext_modules = [Extension('fliteLib', ['flite_lib.c'],
                             include_dirs=inc_dirs,
                             library_dirs=lib_dirs,
                             libraries=['./flite/flite_cmu_us_kal', './flite/flite_usenglish', './flite/flite_cmulex', './flite/flite', 'm'])]
)