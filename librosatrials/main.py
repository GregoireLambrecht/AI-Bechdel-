import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display as ld
import librosa.feature as lf

y, sr = librosa.load('2466.wav')

def fft(segment_time_series):
    fourier=np.abs(librosa.stft(segment_time_series))
    fig, ax=plt.subplots()
    img= ld.specshow(librosa.amplitude_to_db(fourier,ref=np.max), y_axis='log',x_axis='time',ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.show()
    return(fourier)

fft(y)


def melscaling(fourier, sr):
    mel_result= lf.melspectrogram(S=fourier**2,sr=sr)
    print(mel_result)
    fig,ax= plt.subplots()
    S_dB=librosa.power_to_db(mel_result,ref=np.max)
    #img=librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, ax= ax)
    #fig.colorbar(img, ax=ax,format='%+2.0f dB')
    #ax.set(title='Mel-frequency spectrogram')
    #plt.show()
    return (mel_result)

melscaling(fft(y),sr)
# And compute the spectrogram magnitude and phase
