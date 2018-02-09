#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 2 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
#from scipy.signal.waveforms import sawtooth, square
import numpy as np
import matplotlib.patches as mpatches 
from skimage.draw.draw import circle

def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    """
    Create a synthetic 'sine wave'
    First version : use classic Python lists
    a : amplitude
    f : frequence
    omega : pulsation
    t : temps (periode)
    te : periode qu'on souhaite evaluer (ici en milliseconde)
    N : periode entre chacun des points
    ph : phase a l origine 
    sig_t : tableau x (abscisse)
    sig_s : tableau y (ordonnee)
    
    import Signaux.tp1_0 as tp1.0
    
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


def leg(a, f, fe, nT, name):
    if a<0:
        a=a*-1
    str1=""+name+": a="+str(a)+" f="+str(f)+" fe="+str(fe)
    return str1

def plot(inx, iny, title, labell,format='o'):
    plt.plot(inx,iny,format,label=labell)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    #plt.ylim([-1.2, +1.2])
    plt.grid(True)
    
    
if __name__ == '__main__':
    x,y=make_sin(2,f=50.0,fe=1000.0,nT=2)
    w,z=make_sin(-0.5,f=50.0,fe=1000.0,nT=2)
    plot(x,y,'Deux sinusoïdes',leg(2,50.0,1000.0,2,"s1"),'bo')
    plot(w,z,'Deux sinusoïdes',leg(-0.5,50.0,1000.0,2,"s2"),'ro')
    plt.legend()
    plt.show()