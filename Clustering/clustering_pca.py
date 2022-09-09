from sklearn.decomposition import PCA

from resemblyzer import preprocess_wav, VoiceEncoder
from resemblyzer import sampling_rate
from pathlib import Path

from spectralcluster import SpectralClusterer
from spectralcluster import RefinementOptions

import os

import matplotlib.pyplot as plt


def embeds_audio(audio):
    #give the file path to your audio file
    audio_file_path = audio
    wav_fpath = Path(audio_file_path)
    
    wav = preprocess_wav(wav_fpath)
    encoder = VoiceEncoder("cpu")
    _, cont_embeds, wav_splits = encoder.embed_utterance(wav, return_partials=True, rate=16)
    print(cont_embeds.shape)
    
    return cont_embeds

#cont_embeds = embeds_audio("discussion.wav")

def nb_speakers(cont_embeds):
    pca = PCA(n_components=2)

    principalComponents = pca.fit_transform(cont_embeds)

    refinement_options = RefinementOptions(
        gaussian_blur_sigma=1,
        p_percentile=0.95)
                
    clusterer = SpectralClusterer(
        min_clusters=1,
        max_clusters=100,
        refinement_options=refinement_options)  
        
    labels = clusterer.predict(principalComponents)
    return max(labels)

def nb_speakers_file(file):
    audio_list = os.listdir(file)
    nb_speakers_list = []
    for audio in audio_list:
        print(audio)
        audio_path = file + "/" + audio
        cont_embeds = embeds_audio(audio_path)
        nb = nb_speakers(cont_embeds)
        nb_speakers_list.append((nb,audio))
        print(nb)
    return nb_speakers_list

listete = nb_speakers_file("audio_data\Film")
# X = []
# Y = []
# for point in principalComponents:
#     x = point[0] 
#     y = point[1]
#     X.append(x)
#     Y.append(y)
    
# plt.scatter(X,Y)







