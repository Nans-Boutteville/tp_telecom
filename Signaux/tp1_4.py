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


class Triangle(base.GraphBase):

    def __init__(self, a, f, fe, nT=None,duree=None, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT=nT,duree=duree,ph=ph)
        
    def func_scal(self,t):
        return self.a*(4*math.fabs((t/(1/self.f))-math.floor((t/(1/self.f))+0.5))-1.0)
    
    def func_vect(self,t):
        return self.a*(4*np.fabs((t/(1/self.f))-np.floor((t/(1/self.f))+0.5))-1.0)
    
    def func_scipy(self):
        return np.linspace(0, self.duree, self.fe)
    
    '''
    Signal de 50Hz sur 300Hz pour 0.037s
    '''
    '''
    def gen(self):
        t = np.linspace(0, 0.037, 300)
        plt.plot(t, sawtooth(2 * np.pi * 50 * t, 0.5))
       
    ''' 
        
if __name__ == '__main__':
    t = Triangle(3,f=50.0,fe=300.0,nT=2)
    '''
    Utilisation des bibliotheques
    '''
    #t.gen()
    
    '''
    Methode procedurale
    Scalaire : make_sin()
    Vectorielle : make_triangle()
    '''
    #x,y=t.make_sin()
    x,y=t.make_triangle()
    t.plot(x, y,"Un signal triangle",t.leg("SC"), "-bo")
    plt.legend()
    
    plt.show()