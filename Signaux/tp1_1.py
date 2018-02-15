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
    
    '''
    Methode procedurale
    Scalaire : make_sin()
    Vectorielle : make_vect()
    '''
    
    #x,y=s1.make_sin()
    #w,z=s2.make_sin()
    x,y=s1.make_sin_vect()
    w,z=s2.make_sin_vect()
    s1.plot(x,y,'Deux sinusoïdes',s1.leg("s1"),'bo')
    s2.plot(w,z,'Deux sinusoïdes',s2.leg("s2"),'ro')
    plt.legend()
    plt.show()