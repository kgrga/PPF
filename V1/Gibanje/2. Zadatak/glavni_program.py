from kinematika import jed_gib 

#Prim: tijelo mase 2 kg, sila 4 N, početna brzina 0 m/s, početni položaj 0 m
masa = 2       # kg
sila = 4       # N
v0 = 0         # m/s
x0 = 0         # m
t_max = 10     # s

#Pozivanje funkcije iz modula
t, x, v = jed_gib(sila=sila, masa=masa, v0=v0, x0=x0, t_max=t_max)
