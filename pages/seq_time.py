import librosa
import time
y,sr = librosa.load("tetris_piano_mono.wav")
t1 = time.time()
S = librosa.feature.melspectrogram(
    y=y,
    sr=sr,
    n_fft=16384,
    hop_length=128,
    n_mels=8192,
)
t2 = time.time()
print(t2-t1)