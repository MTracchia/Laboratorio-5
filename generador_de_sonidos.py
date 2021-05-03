# -*- coding: utf-8 -*-
"""Generador de sonidos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cg6Xi8URct9ULL8HAGSqMKc8TeK01zOS
"""

import numpy as np
from IPython.lib.display import Audio
from matplotlib import pyplot as plt

SampleRate = 44100 #Hz
play_time_seconds = 10

fs=200.0 #Hz
amplitude = 0.5  #np.iinfo(np.int16).max

time = np.linspace(0, play_time_seconds, SampleRate*play_time_seconds)
data = amplitude*np.sin(2*np.pi*fs*time) 
Audio(data, rate=SampleRate, autoplay=True)

sel = np.abs(time-0) < .05
plt.plot(time[sel], data[sel])
plt.xlabel("Tiempo [segundos]");