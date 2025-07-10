import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
frequency_sampling, audio_signal = wavfile.read("C:/Users/PMLS/Downloads/Audio_waterfall.wav")
print('signal shape:', audio_signal.shape)
print('signal Datatype:', audio_signal.dtype)
print('signal Duration:', round(audio_signal.shape[0]/float (frequency_sampling),2),'seconds')
audio_signal=audio_signal /np.power(2,15)
audio_signal= audio_signal[:100]
time_axis=1000*np.arange(0,len(audio_signal),1) / float(frequency_sampling)
plt.plot(time_axis,audio_signal,color='yellow')
plt.xlabel('Time(miliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()
