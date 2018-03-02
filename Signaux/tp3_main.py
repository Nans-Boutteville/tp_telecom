'''
Created on 23 fevr. 2018
@author: M.Dien
'''
import numpy as np
import matplotlib.pyplot as plt
import Signaux.tp1_usingclasses as base

class Fourier_Signal(base.GraphBase):
    def __init__(self, a, f, fe, nT=None,duree=None, ph=0, o=0, d=0):
        base.GraphBase.__init__(self,a,f,fe,nT=nT,duree=duree,ph=ph,o=o, d=d)
    
    def make_fourier(self):
        base.GraphBase.make_fourier(self)
        
        
if __name__ == '__main__':   
    # make a little extra space between the subplots
    plt.subplots_adjust(wspace=0.5)
    
    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))                 # white noise 1
    nse2 = np.random.randn(len(t))                 # white noise 2
    r = np.exp(-t/0.05)
    
    cnse1 = np.convolve(nse1, r, mode='same')*dt   # colored noise 1
    cnse2 = np.convolve(nse2, r, mode='same')*dt   # colored noise 2
    
    # two signals with a coherent part and a random part
    s1 = 0.01*np.sin(2*np.pi*10*t) + cnse1
    s2 = 0.01*np.sin(2*np.pi*10*t) + cnse2
    N = 15  
    o = 15
    fe = 3000
    d = 0.01
    f = 1000
    #tri = Fourier_Signal(3,f=50.0,fe=300.0, duree=10,o = 10, d=15)
    tri = Fourier_Signal(3, f=300, fe=1000, duree = 15, o=1, d=5)
    xT, yT = tri.make_fourier()
        
    plt.subplot(211)
    plt.plot(t, xT, t, yT)
    plt.xlim(0, 5)
    plt.xlabel('time')
    plt.ylabel('s1 and s2')
    plt.grid(True)
    
    plt.subplot(212)
    cxy, f = plt.cohere(xT, yT, 256, 1./dt)
    plt.ylabel('n')
    plt.show()