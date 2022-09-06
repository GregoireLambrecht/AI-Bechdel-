import librosa
import matplotlib.pyplot as plt
import numpy as np


data, sr = librosa.load("103-1240-0000.flac")

plt.plot([k/sr for k in range(len(data))], data)
plt.show()


#Input : The path (a string) of a file .txt or .rttm 
#The text in a string 

def text_file_to_text(file): 
    text_file = open(file)
    text = text_file.read()
    text_file.close() #Beware to close the file...
    return text

print(text_file_to_text("abjxc.rttm"))