# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:40:16 2016

@author: aminu.mubarak
"""

import GenSignal as gensig
import math as m
import matplotlib.pyplot as plt
#import Queue, threading

def frames (f0,fs,dur,frame_dur):
    #frame = []
    frame_len = frame_dur*fs
    len_frame = int(frame_len)
    sinusoid = gensig.genSine(f0,fs,dur)
    noise = gensig.genNoise(dur)
    signal = gensig.genSignal(sinusoid, noise)  
    N = len(signal)
    num_frames = m.floor(N/len_frame)
    for i in range (num_frames):
        frame = signal[(i)*len_frame+1 : len_frame*(i+1)]
    return frame, signal, sinusoid, noise                  

if __name__ == '__main__':
    
    f0 = 4
    fs = 16000
    dur = 1*fs
    pad = 0.5
    frame_dur = 0.1
    frame, signal, sinusoid, noise = frames(f0,fs,dur,frame_dur)
   
    plt.figure(1)
    plt.plot(signal)
    plt.ylim(signal.min()-pad, signal.max()+pad)
    plt.show()
    
    plt.figure(2)
    plt.plot(sinusoid)
    plt.ylim(sinusoid.min()-pad, sinusoid.max()+pad)
    plt.show()
    
    plt.figure(3)
    plt.plot(noise)
    plt.ylim(noise.min()-pad, noise.max()+pad)
    plt.show()
    
    plt.figure(4)
    plt.plot(frame)
    plt.ylim(frame.min()-pad, frame.max()+pad)
    plt.show()