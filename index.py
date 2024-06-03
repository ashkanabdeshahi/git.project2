import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate?import sounddevice as sd
seconds = 3 # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 


import numpy as np

from scipy.fftpack import fft
from scipy.io import wavfile # get the api
fs, data = wavfile.read('output.wav') # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = len(c)#/2  # you only need half of the fft list (real signal symmetry)
#e=np.array(c)

print (c)
