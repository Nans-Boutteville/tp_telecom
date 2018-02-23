#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 22 fevr. 2018

@author: M.Dien
'''
import Signaux.tp1_0 as tp1_0
import Signaux.tp1_2 as tp1_2
import Signaux.tp1_3 as tp1_3
import Signaux.tp1_4 as tp1_4
import matplotlib.pyplot as plt
from _operator import add

if __name__ == '__main__':
    
    """
    SINUSOIDES
    """
    niv = 0.8
    s = tp1_0.Sinusoide(127.5*niv,440.0,44100.0,nT=None,duree=5)
    do = tp1_0.Sinusoide(127.5*niv,264.0,44100.0,nT=None,duree=5)
    re = tp1_0.Sinusoide(127.5*niv,297.0,44100.0,nT=None,duree=5)
    mi = tp1_0.Sinusoide(127.5*niv,330.0,44100.0,nT=None,duree=5)
    fa = tp1_0.Sinusoide(127.5*niv,352.0,44100.0,nT=None,duree=5)
    sol = tp1_0.Sinusoide(127.5*niv,396.0,44100.0,nT=None,duree=5)
    la = tp1_0.Sinusoide(127.5*niv,440.0,44100.0,nT=None,duree=5)
    si = tp1_0.Sinusoide(127.5*niv,495.0,44100.0,nT=None,duree=5)
    do2 = tp1_0.Sinusoide(127.5*niv,528.0,44100.0,nT=None,duree=5)
    #x,y=s.make_sin()
    #x,y=s.make_sin_vect()
    x,y=s.make_sign_vect()
    y1 = do.make_sign_vect()
    y2 = re.make_sign_vect()
    y3 = mi.make_sign_vect()
    y4 = fa.make_sign_vect()
    y5 = sol.make_sign_vect()
    y6 = la.make_sign_vect()
    y7 = si.make_sign_vect()
    y8 = do2.make_sign_vect()
    a = 100 
    res = map(add, y1, y2, y3, y4, y5, y6, y7, y8)
    #s.plot(x,y,'Une sinusoïde',s.leg("s1"),'-bo')
    res.plot(a, res, 'C9', label='melodie')
    plt.legend()
    plt.show()