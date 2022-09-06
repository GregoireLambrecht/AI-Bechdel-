import librosa
import matplotlib.pyplot as plt

data, sr= librosa.load ('103-1240-0000.flac')
plt.plot(data)
plt.show()
print(sr)