#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 3 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
import Signaux.tp1_0 as tp1_0
    
class Carre:

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
            sig_s.append(2 * self.a * (2.0 * math.floor(self.f * t) - math.floor(2.0 * self.f * t) + 1) - self.a)
        return sig_t, sig_s
    
if __name__ == '__main__':
    """ 
    x=sig_t
    y=sig_s
    """
    c = Carre(3,f=50.0,fe=300.0,nT=3)
    p = tp1_0.Plot()
    x,y=c.make_sin()
    p.plot(x, y,"un signal carré", p.leg(c.a, c.f, c.fe, c.nT, "SC"), "-bo")
    plt.legend()
    plt.show()