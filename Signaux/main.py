'''
Created on 9 févr. 2018

@author: nansboutteville
'''
import Signaux.tp1_0 as tp1_0
import Signaux.tp1_2 as tp1_2
import Signaux.tp1_3 as tp1_3
import Signaux.tp1_4 as tp1_4
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    """
    SINUSOIDES
    """
    s1 = tp1_0.Sinusoide(2,f=50.0,fe=1000.0,nT=2)
    s2=  tp1_0.Sinusoide(-0.5,f=50.0,fe=1000.0,nT=2)
    x,y=s1.make_sin_scal()
    w,z=s2.make_sin_scal()
    s1.plot(x,y,'GRAPHIQUES',s1.leg("s1"),'bo')
    s2.plot(w,z,'GRAPHIQUES',s2.leg("s2"),'ro')
    
    """
    CARRE
    """
    c = tp1_2.Carre(3,f=50.0,fe=300.0,nT=3)
    x,y=c.make_sin_scal()
    c.plot(x, y,"GRAPHIQUES", c.leg("SC"), "-go")
    
    """
    DENT DE SCIE
    """
    dent = tp1_3.DentDeScie(2,f=50.0,fe=1000.0,nT=2)
    x,y=dent.make_sin_scal()
    dent.plot(x, y,"GRAPHIQUES", dent.leg("SC"), "-yo")
    
    """
    TRIANGLE
    """
    t = tp1_4.Triangle(3,f=50.0,fe=300.0,nT=2)
    x,y=t.make_sin_scal()
    t.plot(x, y,"GRAPHIQUES",t.leg("SC"), "-mo")
    
    
    plt.legend()
    plt.show()