'''
Created on 9 févr. 2018

@author: nansboutteville
'''
import math
import matplotlib.pyplot as plt
import numpy as np 

class GraphBase:
    
    def __init__(self, a, f, fe, nT=None, ph=0, duree=None, o=None, d=None):
        self.a=a
        self.ph=ph
        self.f=f
        self.fe=fe
        self.nT=nT
        self.duree=duree
        self.o=o
        self.d=d
        
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
    
    def an_triangle(self, n):
        if n%2==0 :
            return 0
        else : 
            return ((8 * self.a) / np.pi**2) * math.fsum(1/((2*n+1)**2)) #Triangle
            
    def bn_triangle(self, n):
        if n%2==0 :
            return 0
        else :
            return 4/(2*n+1)
        
    def an_dent(self, n):
        if n%2==0 :
            return 0
        else : 
            return ((-2 * self.a)/np.pi)
            
    def bn_dent(self, n):
        if n%2==0 :
            return 0
        else :
            return math.fsum(1/n)
        
    def an_carre(self, n):
        if n%2==0 :
            return 0
        else : 
            return ((2 * self.a) / np.pi) * math.fsum(1/((2*n+1)**2)) 
            
    def bn_carre(self, n):
        if n%2==0 :
            return 0
        else :
            return 4/(2*n+1)
         
    def make_fourier(self): #triangle
        sig_t = np.linspace(self.o, self.d, self.fe*self.d)
        sig_s = sig_t * self.o
        for n in range (2*7) :
            sig_s += self.an_triangle(n)*np.cos(2*np.pi*self.f*sig_t*n)

        return sig_t, sig_s