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

class Sinusoide:

    def __init__(self, a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
        self.a=a
        self.ph=ph
        self.f=f
        self.fe=fe
        self.nT=nT
        
    def make_sin(self):
        omega = 2*math.pi*self.f
        N = int(self.fe/self.f)
        te = 1.0/self.fe
        sig_t = [] 
        sig_s = []
        for i in range(N*self.nT):
            t = te*i
            sig_t.append(t)
            sig_s.append(self.a*math.sin((omega*t)+self.ph))
        
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
    s = Sinusoide(2,50.0,1000.0,2)
    x,y=s.make_sin()
    plot(x,y,"Une sinusoide ...")
    
    plt.show()