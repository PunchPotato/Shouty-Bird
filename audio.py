import sounddevice as sd
import numpy as np
import threading

class Audio():
    def __init__(self) -> None:
        self.sample_rate = 44100
        self.audio = True
        self.quiet_threshold = 0.01
        self.moderate_threshold = 0.03
        self.stream = None
        self.thread = None
        self.latest_amplitude = 0

    def audio_callback(self, indata, frames, time, status):
        if status:
            pass
        amplitude = np.mean(indata)  
        self.latest_amplitude = amplitude 
        self.classify_loudness(amplitude) 

        if not self.audio:
            raise sd.CallbackAbort

    def capture_audio(self):
        self.stream = sd.InputStream(callback=self.audio_callback,
                                     channels=2,
                                     samplerate=self.sample_rate)
        self.stream.start()

    def start_capture_thread(self):
        self.thread = threading.Thread(target=self.capture_audio)
        self.thread.daemon = True
        self.thread.start()

    def stop_capture_thread(self):
        self.audio = False
        if self.thread is not None:
            self.thread.join()

    def classify_loudness(self, amplitude):
        if amplitude < self.quiet_threshold:
            pass
        elif amplitude < self.moderate_threshold:
            pass
        else:
            pass

# Example usage:
audio_instance = Audio()
audio_instance.start_capture_thread()