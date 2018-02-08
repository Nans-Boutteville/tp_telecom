#!usr/bin/python
#-*- coding: utf-8 *-*
'''
Created on 2 fevr. 2018

@author: M.Dien
'''
import math
import matplotlib.pyplot as plt
#from scipy.signal.waveforms import sawtooth, square
import numpy as np
import matplotlib.patches as mpatches 
from skimage.draw.draw import circle

def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    """
    Create a synthetic 'sine wave'
    First version : use classic Python lists
    a : amplitude
    f : frequence
    omega : pulsation
    t : temps (periode)
    te : periode qu'on souhaite evaluer (ici en milliseconde)
    N : periode entre chacun des points
    ph : phase a l origine 
    sig_t : tableau x (abscisse)
    sig_s : tableau y (ordonnee)
    
    import Signaux.tp1_0 as tp1.0
    
    """
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    sig_t = [] 
    sig_s = []
    for i in range(N*nT):
        t = te*i
        sig_t.append(t)
        sig_s.append(a*math.sin((omega*t)+ph))
        
    return sig_t, sig_s

#periode = 1.0
def leg(inx,iny,name):
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
    else:
        if(periode != 0):
         str1 +=" T="+str(periode)+" a="+a + " f="+str(1/periode) +" omega="+str(2*math.pi*(1/periode))
    return str1
   

def plot(inx, iny, title, name,format='o'):
    plt.plot(inx,iny,format,label=leg(inx,iny,name))
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title('Deux sinusoïdes')
    #plt.ylim([-1.2, +1.2])
    plt.grid(True)
    
    
if __name__ == '__main__':
    x,y=make_sin(2,f=50.0,fe=1000.0,nT=2)
    w,z=make_sin(-0.5,f=50.0,fe=1000.0,nT=2)
    plot(x,y,"s1","s1",'bo')
    plot(w,z,"s2","s2",'ro')
    plt.legend()
    plt.show()