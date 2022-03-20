# import pyflite
# import os
# import sys

# if not os.path.exists("cmu_us_rms.flitevox"):
#     print("You need to download a voice to test this.  See the README")
#     sys.exit(1)

# pyflite.init()

# x = pyflite.select_voice("cmu_us_rms.flitevox")
# y = pyflite.text_to_wave("A whole joy was reaping, but they've gone south.", x);

# from array import array
# samples = array('h', y['samples'])
# with open("test.raw", 'wb') as f:
#     samples.tofile(f)

import pyflite
import os
import sys

if not os.path.exists("cmu_indic_hin_ab.flitevox"):
    print("You need to download a voice to test this.  See the README")
    sys.exit(1)

#pyflite.init()

#print("initializing")
#x = pyflite.select_voice("cmu_indic_hin_ab.flitevox")
#x = pyflite.select_voice("cmu_indic_hin_ab.flitevox")
print("select voice")
#y = pyflite.text_to_wave("इस पृष्ठ पर इन्टरनेट पर उपलब्ध विभिन्न हिन्दी एवं देवनागरी सम्बंधित साधनों की कड़ियों की सूची है। इसमें ऑनलाइन एवं ऑफ़लाइन उपकरण (टू>
y = pyflite.text_to_wave("A whole joy was reaping, but they've gone south.");

print("conversion done")
print(y)
from array import array
samples = array('h', y['samples'])
with open('SAI-test.wav', 'wb') as f:
    samples.tofile(f)

print("file written")