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

    def __init__(self, a, f, fe, nT=None,duree=None, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT=nT,duree=duree,ph=ph)

    def func_scal(self,t):
        omega = 2*math.pi*self.f
        return self.a*math.sin((omega*t)+self.ph)
    
    def func_vect(self,t):
        omega = 2*math.pi*self.f
        return self.a*np.sin((omega*t)+self.ph)
    
if __name__ == '__main__':
    s = Sinusoide(2,50.0,1000.0,nT=2,duree=2)
    #x,y=s.make_sin()
    #x,y=s.make_sin_vect()
    x,y=s.make_sign_vect()
    s.plot(x,y,'Une sinusoïde',s.leg("s1"),'-bo')
    plt.legend()
    plt.show()