#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 2 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
import Signaux.tp1_0 as tp1_0

    
if __name__ == '__main__':
    s1 = tp1_0.Sinusoide(2,f=50.0,fe=1000.0,nT=2)
    s2=  tp1_0.Sinusoide(-0.5,f=50.0,fe=1000.0,nT=2)
    x,y=s1.make_sin()
    w,z=s2.make_sin()
    p = tp1_0.Plot()
    p.plot(x,y,'Deux sinusoïdes',p.leg(s1.a, s1.f, s1.fe, s1.nT,"s1"),'bo')
    p.plot(w,z,'Deux sinusoïdes',p.leg(s2.a, s2.f, s2.fe, s2.nT,"s2"),'ro')
    plt.legend()
    plt.show()