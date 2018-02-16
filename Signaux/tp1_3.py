#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 6 févr. 2018

@author: M.Dien
'''

import math
import matplotlib.pyplot as plt
import Signaux.tp1_usingclasses as base
from scipy import signal
import numpy as np
from scipy.signal.waveforms import sawtooth

class DentDeScie(base.GraphBase):

    def __init__(self, a, f, fe, nT=None,duree=None, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT=nT,duree=duree,ph=ph)
        
    def func_scal(self,t):
        return 2*self.a*((t/(1/self.f))-math.floor((t/(1/self.f)))-(0.5))
    
    def func_vect(self,t):
        return 2*self.a*((t/(1/self.f))-np.floor((t/(1/self.f)))-(0.5))
    
    def func_scipy(self):
        return np.linspace(0, self.duree, self.fe)
    
    '''
    Signal de 50Hz sur 1000Hz pour 0.039s
    '''
    '''
    def gen(self):
        t = np.linspace(0, 0.039, 1000)
        plt.plot(t, sawtooth(2 * np.pi * 50 * t))
    '''
if __name__ == '__main__':
    dent = DentDeScie(2,f=50.0,fe=1000.0,nT=2)
    '''
    Utilisation des bibliotheques
    '''
    #dent.gen()
    
    '''
    Methode procedurale
    Scalaire : make_sin()
    Vectorielle : make_sawtooth()
    '''
    #x,y=dent.make_sin()
    x,y=dent.make_sawtooth()
    dent.plot(x, y,"Un signal dent de scie", dent.leg("SC"), "-bo")
    plt.legend()
    
    plt.show()