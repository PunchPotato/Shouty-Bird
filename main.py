import sounddevice as sd
import numpy as np

class Audio():
    def __init__(self) -> None:
        self.sample_rate = 44100
        self.audio = True

    def audio_callback(self, indata, frames, time, status):
        if status:
            pass
        print(np.mean(indata))

        # Check the condition to stop capturing audio
        if not self.audio:
            raise sd.CallbackAbort

    def capture_audio(self):
        with sd.OutputStream(callback=self.audio_callback,
                             channels=2,   # Stereo output
                             samplerate=self.sample_rate):
            while self.audio:
                pass  # Keep running until self.audio == False

# Example usage:
audio_instance = Audio()
audio_instance.capture_audio()