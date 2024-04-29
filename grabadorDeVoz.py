import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

import sounddevice
from scipy.io.wavfile import write


fs=44100 #sample_rate
second=int(input("Enter the time duration in second: ")) #enter your required time..
print("Recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished...\nPlease Check it...")