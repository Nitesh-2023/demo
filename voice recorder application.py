'''voice recorder application that record the voice and save it'''
import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
import numpy as np
import wave
import datetime

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder App")

        self.record_button = tk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_audio, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def start_recording(self):
        self.audio_data = []
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)

        self.stream = sd.InputStream(callback=self.audio_callback, channels=2, dtype=np.int16)
        self.stream.start()

    def stop_recording(self):
        self.stream.stop()
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)

    def audio_callback(self, indata, frames, time, status):
        if status:
            print('Error:', status)
        self.audio_data.extend(indata.copy())

    def save_audio(self):
        current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = filedialog.asksaveasfilename(defaultextension=".wav",filetypes=[("Wave files", "*.wav")],initialfile=f"recorded_audio_{current_date}")

        if filename:
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(2)
                wf.setsampwidth(2)
                wf.setframerate(44100)
                wf.writeframes(np.array(self.audio_data).tobytes())

            print(f"Audio saved to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
