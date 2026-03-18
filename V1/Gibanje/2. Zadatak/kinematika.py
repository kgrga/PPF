import matplotlib.pyplot as plt
import numpy as np


def jed_gib(sila=None, masa=None, v0=0, x0=0, t_max=10, dt=0.1):
    if sila is not None and masa is not None:
        a = sila / masa  #ubrzanje po drugom Newtonovom zakonu
    else:
        a = 0  #jednoliko gibanje bez sile, ubrzanje = 0
    
    #vrijeme
    t = np.arange(0, t_max + dt, dt)
    
    #brzina i položaj
    v = v0 + a * t
    x = x0 + v0 * t + 0.5 * a * t**2
    
    # crtanje grafova
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(t, x, label='x(t)')
    plt.title('Položaj u funkciji vremena')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj (m)')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(1,2,2)
    plt.plot(t, v, 'r', label='v(t)')
    plt.title('Brzina u funkciji vremena')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Brzina (m/s)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    return t, x, v