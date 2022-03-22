import fliteLib
import pyaudio
import wave

waveOutput = fliteLib.textToWave("hi")
print("**************** Output *********")
# print(waveOutput)

waveBytes = b"".join(waveOutput)
print(waveBytes)

wf = wave.open("test.wav", 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

stream.write(waveBytes)
stream.stop_stream()
stream.close()
p.terminate()