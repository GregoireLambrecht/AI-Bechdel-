from pydub import AudioSegment
from clustering import labelling_file

#audio is the audio (ex : "moovie.wav")
#onset is the beginning of the cut in second 
#end the end 
#file is the place where you want to put the new audio (ex : "audio_data")
#file has to exist 


def cut_audio(audio,onset,end,file):
    path_wav = file + "/" + audio[:-4] + "_" + str(onset) + "_" + str(end) + ".wav" #the path of the new audio
    
    onset = onset*1000      #pydub works in millisecond 
    end = end*1000
    
    newAudio = AudioSegment.from_wav(audio) 
    newAudio = newAudio[onset:end]
    newAudio.export(path_wav, format = "wav") 


#audio : the name of the audio
#labelling : the labelling of the audio
#file : the name of the file where put the new audios 
def cut_audio_with_labelling(audio,labelling,file):
    for label in labelling : 
        (indice,onset,end) = label
        if int(indice) != 0 :
            cut_audio(audio,onset,end,file)
            
            
print("hello")
            
            
