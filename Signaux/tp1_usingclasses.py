'''
Created on 9 févr. 2018

@author: nansboutteville
'''
import math
import matplotlib.pyplot as plt
import numpy as np 

class GraphBase:
    
    def __init__(self, a, f, fe, nT=None, ph=0, duree=None):
        self.a=a
        self.ph=ph
        self.f=f
        self.fe=fe
        self.nT=nT
        self.duree=duree
        
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
        
    def concat(self, GraphBase):
        x1,y1 = self.make_sign_vect(self)
        x2,y2 = GraphBase.make_sign_vect(GraphBase)
        resX = x1 + self.duree
        resY = y1 + y2
        return resX, resY
        
    def make_sin_scal(self):
        N = int(self.fe/self.f)
        te = 1.0/self.fe
        sig_t = [] 
        sig_s = []
        if self.nT is not None :
            for i in range(N*self.nT):
                t = te*i
                sig_t.append(t)
                sig_s.append(self.func_scal(t))
        
        return sig_t, sig_s
    
    def make_sign_vect(self):
        N = int(self.fe/self.f)
        te = 1.0/self.fe
        sig_t = [] 
        sig_s = []
        if self.duree is not None :
            sig_t = np.linspace(0, self.duree, self.duree*self.f)
            sig_s = self.func_vect(sig_t)
        
        return sig_t, sig_s
    
