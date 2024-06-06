import sounddevice
from scipy.io.wavfile import write
def savefile(sec):
    print("start")
    recording = sounddevice.rec((sec*44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write("text.wav", 44100, recording)
    print("end")
savefile(10)
