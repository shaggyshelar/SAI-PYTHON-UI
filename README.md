# SAI-PYTHON-UI

On raspbian install following packages
sudo apt-get install swig
sudo ln -s /usr/bin/swig3.0 /usr/bin/swig


To run on Mac
- python3 main.py

To Run Flite
- git  clone https://github.com/festvox/flite
- cd flite
- ./configure --with-audio=alsa --with-vox=awb --enable-shared
- make

To run already created executable flite build
- cd Flite
- `chmod +x flite` ( this is one time )
- `./flite -t "Hello World" -o test.wav`
- aplay test.wav
- `./flite -voice ./voices/cmu_indic_mar_aup.flitevox "आपण निवडलेल्या भाषेमध्ये टाइप करणे सोपे बनवतात" -o marathi.wav`
- aplay marathi.wav

To build `fliteLib` c to python module
`python3 setup.py build`

To install `fliteLib` python module
`sudo python3 setup.py install`

Create installer file
- `pip3 install pyinstaller`
- `python3 -m PyInstaller --onefile --add-data="Flite/test.wav:Flite" --add-data="Flite/A.wav:Flite" --add-data="Flite/B.wav:Flite" --add-data="Flite/X.wav:Flite" --add-data="Flite/Y.wav:Flite" SAI.py`
- go inside "dist" directory

How to use .c files in python
https://book.pythontips.com/en/latest/python_c_extension.html#

Compile file in in .c
`gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c`


To Compile "flite_sample.c" which include flite on MacOS
`gcc -shared -Wl,-install_name,flite_sample -g -o flite_sample.so -fPIC flite_sample.c -I./include -L./build/x86_64-darwin21.1.0/lib -lflite_cmu_us_kal -lflite_usenglish -lflite_cmulex -lflite -lm`

To Compile "flite_sample.c" which include flite on RaspberyPi
`gcc -shared -Wl,-soname,flite_sample -g -o flite_sample.so -fPIC flite_sample.c -I./include -L./build/armv6l-linux-gnueabihf/lib -lflite_cmu_us_kal -lflite_usenglish -lflite_cmulex -lflite -lm -lasound`


To run sample file include "flite_sample.so" file
`python3 flite_sample.py`

Repo for flite c to python

pyflite Python Module
https://github.com/happyalu/pyflite

git clone https://github.com/happyalu/pyflite.git
cd pyflite

git clone https://github.com/happyalu/flite.git
cd flite
./configure --with-audio=alsa --with-vox=awb --enable-shared
make
sudo nano setup.py ( To update flite as per raspbian configs)

`
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
`

`python3 setup.py build`
`sudo python3 setup.py install`
`wget http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_us_rms.flitevox`
`python3 test.py`

http://festvox.org/flite/packed/flite-2.1/voices/