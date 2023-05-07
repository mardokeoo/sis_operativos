from shlex import join
import pyaudio
import wave
import whisper
import os

#VARIABLES
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
DURATION=10
ARCHIVO="audio.wav"

#START PYAUDIO
audio=pyaudio.PyAudio()
stream=audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#START GRABACION
print("inicia grabacion")
frames=[]

for i in range(0, int(RATE/CHUNK*DURATION)):
	data=stream.read(CHUNK)
	frames.append(data)
print("fin grabacion")

#STOP GRABACION
stream.stop_stream()
stream.close()
audio.terminate()

#ARCHIVO AUDIO
waveFile = wave.open(ARCHIVO, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

#IA
model = whisper.load_model("small")
result = model.transcribe(ARCHIVO)

f = open("texto", "a")
f.write(result["text"])

print(result["text"])