import Signaux.tp1_2 as tp1_2
import Signaux.tp1_3 as tp1_3
import Signaux.tp1_4 as tp1_4
import matplotlib.pyplot as plt
from scipy import signal, square
from scipy.signal.waveforms import sawtooth
import numpy as np

if __name__ == '__main__':
    '''
    duree choisie
    '''
    du=0.058
    """
    CARRE
    """
    c = tp1_2.Carre(3,f=50.0,fe=300.0,nT=3,duree=du)
    #x,y=c.func_scipy()
    #c.plot(x, y,"GRAPHIQUES", c.leg("SC"), "-go")
    plt.plot(c.func_scipy(), signal.square(2 * np.pi * 50 * c.func_scipy()),label=c.leg("carre"))
    plt.ylim(-2, 2)
    
    """
    DENT DE SCIE
    """
    dent = tp1_3.DentDeScie(2,f=50.0,fe=1000.0,nT=2,duree=du)
    #x,y=dent.func_scipy()
    #dent.plot(x, y,"GRAPHIQUES", dent.leg("SC"), "-yo")
    plt.plot(dent.func_scipy(), sawtooth(2 * np.pi * 50 * dent.func_scipy()),label=dent.leg("dent"))
    
    """
    TRIANGLE
    """
    t = tp1_4.Triangle(3,f=50.0,fe=300.0,nT=2,duree=du)
    #x,y=t.func_scipy()
    #t.plot(x, y,"GRAPHIQUES",t.leg("SC"), "-mo")
    
    plt.plot(t.func_scipy(), sawtooth(2 * np.pi * 50 * t.func_scipy(), 0.5),label=t.leg("triangle"))
    
    
    plt.legend()
    plt.show()