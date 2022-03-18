# SAI-PYTHON-UI

To run on Mac
- python3 main.py

To Run Flite
- cd Flite
- `chmod +x flite` ( this is one time )
- `./flite -t "Hello World" -o test.wav`
- aplay test.wav
- `./flite -voice ./voices/cmu_indic_mar_aup.flitevox "आपण निवडलेल्या भाषेमध्ये टाइप करणे सोपे बनवतात" -o marathi.wav`
- aplay marathi.wav

Create installer file
- `pip3 install pyinstaller`
- `python3 -m PyInstaller --onefile --add-data="Flite/test.wav:Flite" --add-data="Flite/A.wav:Flite" --add-data="Flite/B.wav:Flite" --add-data="Flite/X.wav:Flite" --add-data="Flite/Y.wav:Flite" SAI.py`
- go inside "dist" directory

How to use .c files in python
https://book.pythontips.com/en/latest/python_c_extension.html#

Compile file in in .c
`gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c`


To Compile "flite_sample.c" which include flite on MacOS
`gcc -shared -Wl,-install_name,adder -g -o flite_sample.so -fPIC flite_sample.c -I./include -L./build/x86_64-darwin21.1.0/lib -lflite_cmu_us_kal -lflite_usenglish -lflite_cmulex -lflite -lm`

To run sample file include "flite_sample.so" file
`python3 flite_sample.py`
