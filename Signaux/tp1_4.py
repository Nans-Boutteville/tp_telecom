#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 6 févr. 2018

@author: M.Dien
'''

import math
import matplotlib.pyplot as plt
import Signaux.tp1_usingclasses as base
import numpy as np 


class Triangle(base.GraphBase):

    def __init__(self, a, f, fe, nT, ph=0):
        base.GraphBase.__init__(self,a,f,fe,nT,ph)
        
    def func(self,t):
        return self.a*(4*math.fabs((t/(1/self.f))-np.floor((t/(1/self.f))+0.5))-1.0)
        
if __name__ == '__main__':
    t = Triangle(3,f=50.0,fe=300.0,nT=2)
    x,y=t.make_sin()
    t.plot(x, y,"Un signal triangle",t.leg("SC"), "-bo")
    plt.legend()
    plt.show()