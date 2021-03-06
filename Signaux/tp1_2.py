#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 3 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
import Signaux.tp1_usingclasses as base
from scipy import signal, square
import numpy as np
    
class Carre(base.GraphBase):

    def __init__(self, a, f, fe, nT=None,duree=None, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT=nT,duree=duree,ph=ph)
        
    def func_scal(self,t):
        return 2 * self.a * (2.0 * math.floor(self.f * t) - math.floor(2.0 * self.f * t) + 1) - self.a
    
    def func_vect(self,t):
        return 2 * self.a * (2.0 * np.floor(self.f * t) - np.floor(2.0 * self.f * t) + 1) - self.a
    
    def func_scipy(self):
        return np.linspace(0, self.duree, self.fe, endpoint=False) 
    
    '''
    Signal de 50Hz sur un echantillan de 300Hz pour 0.058s
    '''
    '''
    def gen(self):
        t = np.linspace(0, 0.058, 300, endpoint=False)
        plt.plot(t, signal.square(2 * np.pi * 50 * t))
        plt.ylim(-2, 2)
    '''
    
if __name__ == '__main__':
    
    c = Carre(3,f=50.0,fe=300.0,nT=3)
    '''
    Utilisation des bibliotheques
    '''
    #c.gen()
    
    """ 
    Methode procedurale
    x=sig_t
    y=sig_s
    """
    '''
    Scalaire : make_sin()
    Vectorielle : make_square()
    '''
    #x,y=c.make_sin()
    x,y=c.make_square()
    c.plot(x, y,"un signal carré", c.leg("SC"), "-bo")
    plt.legend()
    
    plt.show()