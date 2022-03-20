from distutils.core import setup, Extension

import os

try:
    inc_dirs = [os.environ['FLITE_INC'],]
except KeyError:
    inc_dirs=['flite/include']

try:
    lib_dirs = [os.environ['FLITE_LIBS'],]
except KeyError:
    lib_dirs=['flite/build/armv6l-linux-gnueabihf/lib']

setup(name='pyflite',
      version='0.1',
      ext_modules=[Extension('_pyflite', ['pyflite.i', 'pyflite.c'],
                             include_dirs=inc_dirs,
                             library_dirs=lib_dirs,
                             libraries=['flite_cmu_us_kal', 'flite_usenglish', 'flite_cmulex', 'flite', 'asound', 'm'],
                             swig_opts=['-Iflite/include'])],
      py_modules=['pyflite']
)