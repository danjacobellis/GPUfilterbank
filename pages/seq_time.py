import librosa
import numpy as np
import time
y,sr = librosa.load("three_minute_warning.wav")
for N in [2**15,2**18,2**22,2**26]:
    t1 = time.time()
    x_i = y[0:N]
    S = librosa.feature.melspectrogram(
        y=x_i,
        sr=sr,
        n_fft=2^20,
        hop_length=32,
        n_mels=512,
    )
    t2 = time.time()
    print(t2-t1,"\n")
    
    t1 = time.time()
    y_rec = librosa.feature.inverse.mel_to_audio(
        M=S,
        sr=sr,
        n_fft=2^20,
        hop_length=32,
    )
    t2 = time.time()
    print(t2-t1,"\n")