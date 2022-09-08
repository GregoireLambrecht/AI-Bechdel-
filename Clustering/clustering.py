from resemblyzer import preprocess_wav, VoiceEncoder
from resemblyzer import sampling_rate
from pathlib import Path

from spectralcluster import SpectralClusterer
from spectralcluster import RefinementOptions

import os


def diarization_audio(audio):
    #give the file path to your audio file
    audio_file_path = audio
    wav_fpath = Path(audio_file_path)
    
    wav = preprocess_wav(wav_fpath)
    encoder = VoiceEncoder("cpu")
    _, cont_embeds, wav_splits = encoder.embed_utterance(wav, return_partials=True, rate=16)
    print(cont_embeds.shape)
    
    
    refinement_options = RefinementOptions(
        gaussian_blur_sigma=1,
        p_percentile=0.95)
        
    clusterer = SpectralClusterer(
        min_clusters=1,
        max_clusters=100,
        refinement_options=refinement_options)  
    
    labels = clusterer.predict(cont_embeds)
    return labels, wav_splits

#labels, wav_splits = diarization_audio("name.wav")

def create_labelling(labels,wav_splits):
    times = [((s.start + s.stop) / 2) / sampling_rate for s in wav_splits]
    labelling = []
    start_time = 0

    for i,time in enumerate(times):
        if i>0 and labels[i]!=labels[i-1]:
            temp = [str(labels[i-1]),start_time,time]
            labelling.append(tuple(temp))
            start_time = time
        if i==len(times)-1:
            temp = [str(labels[i]),start_time,time]
            labelling.append(tuple(temp))

    return labelling
  
#labelling = create_labelling(labels,wav_splits)

def labelling_file(file):
    audio_list = os.listdir(file)
    labelling_list = []
    for audio in audio_list:
        print(audio)
        if int(audio[:-4]) <= 300:
            audio_path = file + "/" + audio
            labels, wav_splits = diarization_audio(audio_path)
            labelling_list.append(create_labelling(labels,wav_splits))
    return labelling_list


labelling_list = labelling_file("audio_data\Film")
print(labelling_list)


























