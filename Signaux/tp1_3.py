#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 6 févr. 2018

@author: M.Dien
'''

import math
import matplotlib.pyplot as plt
import Signaux.tp1_usingclasses as base

class DentDeScie(base.GraphBase):

    def __init__(self, a, f, fe, nT, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT,ph)
        
    def func(self,t):
        return 2*self.a*((t/(1/self.f))-math.floor((t/(1/self.f)))-(0.5))

if __name__ == '__main__':
    dent = DentDeScie(2,f=50.0,fe=1000.0,nT=2)
    x,y=dent.make_sin()
    dent.plot(x, y,"Un signal dent de scie", dent.leg("SC"), "-bo")
    plt.legend()
    plt.show()