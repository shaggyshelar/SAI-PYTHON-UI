import wave
w = wave.open('testFromC.wav', 'r')
#w = wave.open('SAI-test.wav', 'r')
for i in range(w.getnframes()):
    frame = w.readframes(i)
    print(frame)