'''
Created on 9 févr. 2018

@author: nansboutteville
'''
import math
import matplotlib.pyplot as plt
import numpy as np 

class GraphBase:
    
    def __init__(self, a, f, fe, nT, ph=0):
        self.a=a
        self.ph=ph
        self.f=f
        self.fe=fe
        self.nT=nT
        
    def leg(self, name):
        t=self.a
        if self.a<0:
            t=self.a*-1
        str1=""+name+": a="+str(t)+" f="+str(self.f)+" fe="+str(self.fe)
        return str1

    def plot(self,inx, iny, title, labell,format='o'):
        plt.plot(inx,iny,format,label=labell)
        plt.xlabel('time (s)')
        plt.ylabel('voltage (V)')
        plt.title(title)
        plt.grid(True)
        
    def func(self,t):
        omega = 2*math.pi*self.f
        return self.a*math.sin((omega*t)+self.ph)
        
    def make_sin(self):
        N = int(self.fe/self.f)
        te = 1.0/self.fe
        sig_t = [] 
        sig_s = []
        for i in range(N*self.nT):
            t = te*i
            sig_t.append(t)
            sig_s.append(self.func(t))
        
        return sig_t, sig_s
    
    
