#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 6 févr. 2018

@author: M.Dien
'''

import math
import matplotlib.pyplot as plt
import Signaux.tp1_0 as tp1_0
import numpy as np 
from blaze.expr.expressions import label


class Triangle:

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
            sig_s.append(self.a*(4*math.fabs((t/(1/self.f))-np.floor((t/(1/self.f))+0.5))-1.0))
        return sig_t, sig_s

    
  
if __name__ == '__main__':
    t = Triangle(3,f=50.0,fe=300.0,nT=2)
    p = tp1_0.Plot()
    x,y=t.make_sin()
    p.plot(x, y,"Un signal triangle",p.leg(t.a, t.f, t.fe, t.nT, "SC"), "-bo")
    plt.legend()
    plt.show()