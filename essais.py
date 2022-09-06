import librosa
import matplotlib.pyplot as plt

data, sr = librosa.load("103-1240-0000.flac")

plt.plot([k/sr for k in range(len(data))], data)
plt.show()

