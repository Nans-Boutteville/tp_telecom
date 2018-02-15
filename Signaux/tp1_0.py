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
import Signaux.tp1_usingclasses as base
#from scipy.signal.waveforms import sawtooth, square
import numpy as np 



class Sinusoide(base.GraphBase):

    def __init__(self, a, f, fe, nT, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT,ph)

    def func_scal(self,t):
        omega = 2*math.pi*self.f
        return self.a*math.sin((omega*t)+self.ph)
    
    def func_vect(self,t):
        omega = 2*math.pi*self.f
        return self.a*np.sin((omega*t)+self.ph)
    
    def make_sin_vect(self):
        N = int(self.fe/self.f)
        te = 1.0/self.fe
        sig_t = [] 
        sig_s = []
        for i in range(N*self.nT):
            t = te*i
            sig_t.append(t)
            sig_s.append(self.func_vect(t))
        
        return sig_t, sig_s
    
if __name__ == '__main__':
    s = Sinusoide(2,50.0,1000.0,2)
    #x,y=s.make_sin()
    x,y=s.make_sin_vect()
    s.plot(x,y,'Une sinusoïde',s.leg("s1"),'-bo')
    
    plt.show()