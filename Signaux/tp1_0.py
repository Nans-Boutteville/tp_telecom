#!usr/bin/python
#-*- coding: utf-8 *-*
'''
File : tp1_0.py
Created on 28 fevr. 2012
@author: menez
Creer un signal numerique et l'afficher
On utilise ici le B,A,BA de Python 
    => Donc ca doit etre compris !!!!
'''
import math
import matplotlib.pyplot as plt
#from scipy.signal.waveforms import sawtooth, square
import numpy as np 

def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    """
    Create a synthetic 'sine wave'
    First version : use classic Python lists
    N : 
    """
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    sig_t = [] 
    sig_s = []
    for i in range(N*nT):
        t = te*i
        sig_t.append(t)
        sig_s.append(a*math.sin((omega*t)+ph))
        
    return sig_t, sig_s

def plot(inx, iny, title, format='-bo'):
    plt.plot(inx,iny,format)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    #plt.ylim([-1.2, +1.2])
    plt.grid(True)

    
if __name__ == '__main__':
    x,y=make_sin(2,f=50.0,fe=1000.0,nT=2)
    plot(x,y,"Une sinusoide ...")
    
    plt.show()