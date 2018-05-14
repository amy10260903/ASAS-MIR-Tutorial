# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:04:10 2018

@author: GUANYI
"""

import math
import wave
import struct
import librosa
import numpy as np

def synthComplex(freq=[440, 440, 440], chordResult = [0.,2.,'C:maj'], fname="test.wav", 
                 music = "test.wav",frate = 44100,chordOn=False,cmRatio = 0.3):
    
    ########## Chord Template ##########
    
    # Chroma freq   -> C3 C3# ... B3
    
    noteFreq3 = np.array([[130.81,138.59,146.83,155.56,164.81,174.61,
                          185.00,196.00,207.65,220.00,233.08,246.94]]).T
    noteFreq4 = np.array([[261.63,277.18,293.66,311.13,329.63,349.23,
                          369.99,392.00,415.30,440.00,466.16,493.88]]).T
    noteFreq = noteFreq4
        
    cMajor = np.array([[1,0,0,0,1,0,0,1,0,0,0,0]]).T 
    cMinor = np.array([[1,0,0,1,0,0,0,1,0,0,0,0]]).T
    cMaDe = np.array([1,2,3,5,6,8,9,10,11])
    cMiDe = np.array([1,2,4,5,6,8,9,10,11])
    
    chordName = np.array(['C:maj','C#:maj','D:maj','D#:maj','E:maj','F:maj',
                 'F#:maj','G:maj','G#:maj','A:maj','A#:maj','B:maj',
                 'C:min','C#:min','D:min','D#:min','E:min','F:min',
                 'F#:min','G:min','G#:min','A:min','A#:min','B:min','N'])
    
    template = np.delete(cMajor*noteFreq,cMaDe).reshape((3,1))
    for i in range(11):
        template = np.concatenate( ( template, np.delete(np.roll(cMajor,i+1,axis=0)*noteFreq, 
                                                        ((np.roll(cMaDe,i+1,axis=0)+i+1)%12) ).reshape((3,1)) ), axis=1)
    for i in range(12):
        template = np.concatenate( ( template, np.delete(np.roll(cMinor,i,axis=0)*noteFreq,
                                                        ((np.roll(cMiDe,i,axis=0)+i)%12) ).reshape((3,1)) ) , axis=1)

    ########## Synthesis ##########

    amp=25000.0 
    coef = [0.4,0.3,0.3]
    sine_list=[]
    click_times = []
    
    # Data of sound
    
    for i in range(len(chordResult)):
        
        click_times.append(chordResult[i][0])
        
        datasize = int((chordResult[i][1] - chordResult[i][0]) * frate)
        iChord = np.where(chordName == chordResult[i][2])[0][0]
        #print(chordResult[i][2],iChord)
        if iChord == 24:
            freq = np.array([0.,0.,0.])
        else:    
            freq = template[:,iChord]
        
        for x in range(datasize):       # length of the audio files
            samp = 0
            for k in range(len(freq)):  # produce different frequency of the current time
                samp = samp + coef[k] * math.sin(2*math.pi*freq[k]*(x/frate))
            sine_list.append(samp)  # three freq
    
    ########## Write wav file ##########
    
    print('Wrtie Wav File')
    wav_file=wave.open(fname,"w")
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes=datasize
    comptype= "NONE"
    compname= "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    for s in sine_list:
        wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.close()
        
    yc, sr_c = librosa.load(fname, sr=None)        
    ym, sr_m = librosa.load(music, sr=None)
    
    if len(yc) < len(ym):
        yc = np.concatenate((yc,(np.float32(np.zeros(len(ym)-len(yc))))))
    else:
        ym = np.concatenate((ym,(np.float32(np.zeros(len(yc)-len(ym))))))
    
    clicks = librosa.clicks(click_times, sr = sr_c, length=len(yc))
    
    if chordOn:
        ym_c = (yc+cmRatio*ym) + clicks
    else:                 
        ym_c = ym + clicks
        
    librosa.output.write_wav(fname, ym_c, sr_m)
        
