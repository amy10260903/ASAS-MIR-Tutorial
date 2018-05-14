# ASAS Tutorial - MIR

The goal of this tutorial is to let you understand the concept of music information retreival (MIR), its toolbox, Librosa and Madmom, and implementation of the functions in toolbox.

Due Date: 2018/05/12

## Overview
The tutorial is related to 
> Music Information Retrieval  
> Librosa  
> Madmom  
> Beat Tracking    
> Chord Detection   

## Documents

Please look at the documents below in order to understand the concepts of MIR, MIR toolbox, the code and the homework. 

* [Tutorial PPT](https://docs.google.com/presentation/d/1DbQDEw_j4ZasM3ywzMdGcfkyMYt1ZDAAWIULfyNwDRE/edit?usp=sharing)
* [Librosa](https://hackmd.io/BSdk7rjRRWWZf0ifZIAOwA#)
* [Madmom](https://github.com/bobolee1239/ASAS/blob/master/madmom.md)
* [Beat Tracking](https://docs.google.com/presentation/d/1DbQDEw_j4ZasM3ywzMdGcfkyMYt1ZDAAWIULfyNwDRE/edit?usp=sharing)
* [Chord Detection](https://docs.google.com/presentation/d/1DbQDEw_j4ZasM3ywzMdGcfkyMYt1ZDAAWIULfyNwDRE/edit?usp=sharing) (Options:  [notes](https://drive.google.com/file/d/1T6T-45uemqPi72cfWbH5wUn9zL10bhYL/view?usp=sharing), [paper](https://arxiv.org/pdf/1612.05065.pdf) )

## Installation

Before doing homework, please install the packages below.

* Python (or Anaconda)
* Librosa 
* Madmom  

## Homework

### Q1 : Beat Tracking

1. Beat tracking in Librosa
	* Generate a different kind of tempo (twice, third, one half, or one third ...) for "Demo.mp3"
	* Add clicks for output beat times and write it to an audio file. 
	* Discuss what the code is doing and the corresponding principle at Step 2: Beat tracking
	* [link](https://github.com/jkang3322/ASAS-MIR-Tutorial/blob/master/beat_tracking/beat_track_librosa.ipynb)
2. Beat tracking in Madmom
	* Generate a suitable tempo for "Chopin Nocturne Op. 62 No. 2 in E.mp3" 
	* Add clicks for output beat times and write it to an audio file. 
	* Discuss what the code is doing and the corresponding principle at Step 2: Beat tracking
	* [link](https://github.com/jkang3322/ASAS-MIR-Tutorial/blob/master/beat_tracking/beat_track_madmom.ipynb)

### Q2 : Chord Detection (Madmom)

1. Briefly describe the algorithm of chord detection in madmom.	
2. Use one of your own music wave file (30 s) and run the chord detection. What's the results? Please give some discussion on the results. [link](https://github.com/jkang3322/ASAS-MIR-Tutorial/blob/master/Chord_Detection/chord.py)

### Submission

Please put the files (wave files and pdf) into a folder and submit to ilms.

1. Q1 : 2 output wave files and discussion
2. Q2 : your own music wave file and discussion

