import pyaudio
import numpy as np


class audio():
    def __init__(self) -> None:
        self.p = pyaudio.PyAudio()
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.stream = None

    def device_output_info(self):
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            print(f"Device {i}: {info['name']}")
        for i in range(self.p.get_device_count()):
            dev = self.p.get_device_info_by_index(i)
            print((i,dev['name'],dev['maxInputChannels']))

    def capture_audio_data(self):
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        input_device_index= 4,
                        frames_per_buffer=self.CHUNK)
    
    def read_audio_data(self):
        if self.stream is not None:
            self.data = self.stream.read(self.CHUNK)
            audio_signal = np.frombuffer(self.data, dtype=np.int16)
            rms = np.sqrt(np.mean(audio_signal**2))
            print(rms)
        else:
            print("Stream is not initialized. Call capture_audio_data() first.")

class user_interface():
    pass

audio_instance = audio()
audio_instance.capture_audio_data()
audio_instance.read_audio_data()
