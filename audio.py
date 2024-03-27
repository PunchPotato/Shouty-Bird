import sounddevice as sd
import numpy as np

class Audio():
    def __init__(self) -> None:
        self.sample_rate = 44100
        self.audio = True
        self.quiet_threshold = 0.01
        self.moderate_threshold = 0.04

    def audio_callback(self, indata, frames, time, status):
        if status:
            pass
        amplitude = np.mean(indata)  
        self.classify_loudness(amplitude) 

        if not self.audio:
            raise sd.CallbackAbort

    def capture_audio(self):
        with sd.InputStream(callback=self.audio_callback,
                             channels=2,   
                             samplerate=self.sample_rate):
            while self.audio:
                pass  

    def classify_loudness(self, amplitude):
        if amplitude < self.quiet_threshold:
            print("Quiet")
        elif amplitude < self.moderate_threshold:
            print("Moderate")
        else:
            print("Loud")

# Example usage:
audio_instance = Audio()
