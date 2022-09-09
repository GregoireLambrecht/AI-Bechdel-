import librosa
import matplotlib.pyplot as plt
import librosa.display as ld
import librosa.feature as lf
import os
from statistics import mean
import numpy as np
from sklearn.linear_model import LogisticRegression

# On exploite le fichier txt pour avoir le sexe de la personne qui parle dans les fichiers .flac
file = open("SPEAKERS_librispeech.TXT")

for i in range(0, 12):
    file.readline()

# le dictionnaire suivant a pour clés le numéro d'enregistrement et fait correspondre le sexe de la personne qui parle
number_sex_identification = {}
for line in file.readlines():
    split_line = line.split(" | ")
    number_sex_identification[int(split_line[0])] = split_line[1]


# fonction qui renvoie la transformée de Fourier d'un segment
# segment_time_series est des relevés d'amplitudes de l'onde sonore en fonction du temps (resultat de la fonction librosa.load)
def fft(segment_time_series):
    fourier = np.abs(librosa.stft(segment_time_series))
    return fourier

#fonction qui affiche la transformée de Fourier
def plot_fft(fourier):
    fig, ax = plt.subplots()
    img = ld.specshow(librosa.amplitude_to_db(fourier, ref=np.max), y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Fourier spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.show()
    return


# Fonction qui fait passer à l'échelle MEL la transformée de Fourier, sr la fréquence d'échantillonage
def melscaling(fourier, sr):
    mel_result = lf.melspectrogram(S=fourier ** 2, sr=sr)
    return mel_result

# Fonction qui affiche le spectrogramme de MEL
def plot_mel(mel_spectrogram):
    fig, ax = plt.subplots()
    s_db = librosa.power_to_db(mel_result, ref=np.max)
    img = librosa.display.specshow(s_db, x_axis='time',y_axis='mel', sr=sr,fmax=8000, ax=ax)
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    ax.set(title='Mel-frequency spectrogram')
    plt.show()
    return

# Pour entraîner le modèle, on veut les spectrogrammes sous la forme de vecteurs de même dimension
# Pour cela, on fait la moyenne sur les coefficients dans le temps, donc sur les lignes
def average(melspectrogram):
    result = []
    for i in range(len(melspectrogram)):
        result.append(mean(melspectrogram[i]))
    return result

# On construit les données sur lesquelles la machine est entraînée
X_train = []
Y_train = []
# On parcourt le dossier dans lequel sont situés les fichiers .flac
directory = 'C:/Users/liuce/AI-Bechdel-/flac_files'
for filename in os.listdir(directory):
    data, sr = librosa.load(filename)
    X_train.append(average(melscaling(fft(data), sr)))
    # On retrouve le numéro de l'enregistrement pour ensuite lui faire correspondre le bon sexe
    number = int(filename.split("-")[0])
    Y_train.append(number_sex_identification[number])

# On a choisi un modèle simple de classification linéaire
model = LogisticRegression()
model.fit(X_train, Y_train)
model.predict(X_train)
