#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 6 févr. 2018

@author: M.Dien
'''

import math
import matplotlib.pyplot as plt
import Signaux.tp1_1 as tp1_1
import Signaux.tp1_2 as tp1_2
#from scipy.signal.waveforms import sawtooth, square
import numpy as np 
from blaze.expr.expressions import label
"""
ph = phase a l'origine
sig_t = valeurs dans l'absisses x
sig_s = valeurs dans l'ordonn�e y
N = la periode entre chaque point (temps max/frequence)
te = la periode en seconde que l'on veut evaluer
fe = la periode en milisecode que l'on veut evaluer
t = temps
omega = la pulsation en radian
a = l'amplitude 
f= frequence
"""
def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=3):
    """
    Create a synthetic 'square wave'
    First version : use classic Python lists
    """
    make_sin.frequence = f
    make_sin.fe = fe
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    sig_t = [] 
    sig_s = []
    for i in range(N*nT):
        t = te*i
        sig_t.append(t)
        sig_s.append(a*(4*math.fabs((t/(1/f))-np.floor((t/(1/f))+0.5))-1.0))
    return sig_t, sig_s
    
  
if __name__ == '__main__':
    """ 
    x=sig_t
    y=sig_s1
    """
    x,y=make_sin(3,f=50.0,fe=1000.0,nT=2)
    #plot2(x,y,"Un signal dent de scie","s1","-bo")
    tp1_1.plot(x, y,"Un signal triangle", tp1_1.leg(3, 50.0, 1000.0, 2, "SC"), "-bo")
    plt.legend()
    plt.show()