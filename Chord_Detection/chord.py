# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:40:02 2018

# MIR tutorial for ASAS

@author: GUANYI
"""


import numpy as np
import librosa
import pyaudio
from madmom.audio.signal import Signal
from madmom.audio.chroma import DeepChromaProcessor
from madmom.features.chords import DeepChromaChordRecognitionProcessor

from chordGenerate import synthComplex

musicFile = 'YourInputFile.wav'   # Input Music File
outFile = 'YourOutputFile.wav'                     # Output Music File
playFile = False                            # Play output File immediately

chordOn = True                              # Add the chord sound to output
cmRatio = 0.3                               # Chord and music file sound ratio

##### Chord Detection #####

dcp = DeepChromaProcessor()
decode = DeepChromaChordRecognitionProcessor()

chroma = dcp(musicFile)
output = decode(chroma)

sig = Signal(musicFile, num_channels=1)
    
synthComplex(chordResult = output, fname=outFile, 
             music=musicFile, frate=sig.sample_rate,
             cmRatio = cmRatio, chordOn = chordOn)
   
##### Print Results #####

print('\n######## Results ######\n')
for i in range(len(output)):
    print('start time',output[i][0],'end time',output[i][1],'result',output[i][2])

##### Play Sound #####

if playFile:
    data, fs = librosa.load(outFile,sr=None)
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paFloat32, channels = 1, rate = fs, output = True)
    stream.write(data.astype(np.float32).tostring())

###### PPT ######

# what's chord -> wave file -> different feelings
# chord detection method in madmom trace

# madmom pip install windows (visual C++)

###### To Do List for Code ######

# Visualization of chord -> wave file segment?
# Add click to the chord changing time
# Add handmade chord sound (option)

###### Homework ######

# Describe the algorithm of the functions
# parameters ?
# What's the results on different type of music (choose 2 files for 5 genre)
# Any imrpovement techniques