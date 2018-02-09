#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 3 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
import Signaux.tp1_usingclasses as base
    
class Carre(base.GraphBase):

    def __init__(self, a, f, fe, nT, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT,ph)
        
    def func(self,t):
         return 2 * self.a * (2.0 * math.floor(self.f * t) - math.floor(2.0 * self.f * t) + 1) - self.a
    
if __name__ == '__main__':
    """ 
    x=sig_t
    y=sig_s
    """
    c = Carre(3,f=50.0,fe=300.0,nT=3)
    x,y=c.make_sin()
    c.plot(x, y,"un signal carré", c.leg("SC"), "-bo")
    plt.legend()
    plt.show()