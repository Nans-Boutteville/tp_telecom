#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 3 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
import Signaux.tp1_1 as tp1_1
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
def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
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
        #sig_s.append(a*np.sign(math.sin((omega*t)+ph)))
        #sig_s.append(a*(2*math.floor(f*t)-math.floor(2*f*t)+1))
        #sig_s.append((-1)*math.exp(math.floor(f*t)))
        sig_s.append(2 * a * (2.0 * math.floor(f * t) - math.floor(2.0 * f * t) + 1) - a)
        
    return sig_t, sig_s

def leg2(inx,iny,name):
    str1=""+name+": "
    periode = 0.0;
    fait=0;
    int = -1
    for i in iny:
        int=int+1
        #print(i)
        if round(i,2)==round(iny[0],2) and int>0 :
            if fait==0:
                print("test")
                fait=1
            else :
             periode = inx[int]
             break

    a=str(max(iny))
    if(iny[1]<0 and periode != 0):
        str1 +=" T="+str(periode)+" a=-"+a + " f="+str(1/periode) +" omega="+str(2*math.pi*(1/periode))
    elif(periode != 0): 
        if(periode != 0):
         str1 +=" T="+str(periode)+" a="+a + " f="+str(1/periode) +" omega="+str(2*math.pi*(1/periode))
    else:
        str1 +=" a="+a + " f="+str(make_sin.frequence) + " fe=" + str(make_sin.fe)
             
    return str1

def plot2(inx, iny, title, name,format='o'):
    plt.plot(inx,iny,format,label=leg2(inx,iny,name))
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title('Un signal carré')
    #plt.ylim([-1.2, +1.2])
    plt.grid(True)
    
if __name__ == '__main__':
    """ 
    x=sig_t
    y=sig_s
    """
    x,y=make_sin(3,f=50.0,fe=1000.0,nT=3)
    #tp1_1.plot(x, y, tp1_1.leg(3, 50.0, 1000.0, 3, "SC"), "-bo")
    tp1_1.plot(x, y,"un signal carré", tp1_1.leg(3, 50.0, 1000.0, 3, "SC"), "-bo")
    plt.legend()
    plt.show()