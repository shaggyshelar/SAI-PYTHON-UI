import fliteLib
import pyaudio
import wave
import time
p = pyaudio.PyAudio()

waveOutput = fliteLib.textToWave("countries accepted India's position on conflict in Ukraine")
print("**************** Output *********")
# print(waveOutput)

waveBytes = b"".join(waveOutput)
#print(waveBytes)

wf = wave.open("test.wav", 'rb')
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

stream.write(waveBytes)
time.sleep(5)

print(" ******** Closing  *********")
stream.stop_stream()
stream.close()
p.terminate()