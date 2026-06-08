import numpy as np
import matplotlib.pyplot as plt

#tablica
h0 = 0.54  # m (ukupna visina)
m = 0.5257  # kg
r = 4.025e-3  # m (polumjer osovine)
g = 9.81  # m/s^2
h = np.array([0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40])  # m
t = np.array([1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813])  # s

s = h0 - h



#a)
#log(s) - log(t)
#log(s) = 2*log(t) + log(aef/2)
#fit: y = a*x + b; x = log(t), y = log(s)

log_t = np.log(t)
log_s = np.log(s)
n = len(t)

#lin regresija formulom najmanjih kvadrata
suma_x  = np.sum(log_t)
suma_y  = np.sum(log_s)
suma_xy = np.sum(log_t * log_s)
suma_x2 = np.sum(log_t**2)

a_log = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x**2)
b_log = (suma_y - a_log * suma_x) / n

#pogreske
y_fit = a_log * log_t + b_log
reziduali = log_s - y_fit
sigma2 = np.sum(reziduali**2) / (n - 2)
D = n * suma_x2 - suma_x**2
da_log = np.sqrt(n * sigma2 / D)
db_log = np.sqrt(suma_x2 * sigma2 / D)

print("a) Log-log prikaz")
print(f"Nagib  a = {a_log:.4f} ± {da_log:.4f}")
print(f"Odsječak b = {b_log:.4f} ± {db_log:.4f}")

#b = log(aef/2) => aef = 2 * exp(b)
aef_log = 2 * np.exp(b_log)
daef_log = 2 * np.exp(b_log) * db_log
print(f"aef = {aef_log:.4f} ± {daef_log:.4f} m/s²")


plt.figure(figsize=(7, 5))
plt.scatter(log_t, log_s, color='blue', label='Mjerenja', zorder=5)
x_line = np.linspace(min(log_t), max(log_t), 200)
plt.plot(x_line, a_log * x_line + b_log, color='teal',
         label=f'Fit: a={a_log:.3f}, b={b_log:.3f}')
plt.xlabel('log(t)')
plt.ylabel('log(s)')
plt.title('a) Log-log prikaz pada diska')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('1a.png', dpi=150)
plt.show()



#b)
#s - t2
#s = (aef/2) * t²  =>  s = A * t²  (fit kroz ishodište b=0)
#a = sum(xi*yi) / sum(xi²), xi = t², yi = s

t2 = t**2

a_st2 = np.sum(t2 * s) / np.sum(t2**2)

#pogreška nagiba
y_fit2 = a_st2 * t2
reziduali2 = s - y_fit2
sigma2_st2 = np.sum(reziduali2**2) / (n - 1)
da_st2 = np.sqrt(sigma2_st2 / np.sum(t2**2))

aef_st2 = 2 * a_st2
daef_st2 = 2 * da_st2

print("\nb) s - t² prikaz")
print(f"Nagib  A = {a_st2:.6f} ± {da_st2:.6f} m/s²")
print(f"aef = {aef_st2:.4f} ± {daef_st2:.4f} m/s²")


plt.figure(figsize=(7, 5))
plt.scatter(t2, s, color='blue', label='Mjerenja', zorder=5)
x_line2 = np.linspace(0, max(t2), 200)
plt.plot(x_line2, a_st2 * x_line2, color='teal',
         label=f'Fit: A={a_st2:.5f} m/s²')
plt.xlabel('t² (s²)')
plt.ylabel('s (m)')
plt.title('b) s - t² prikaz pada diska')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('1b.png', dpi=150)
plt.show()



#c)
#Moment tromosti Iz
#aef = m*g*r² / (m*r² + Iz) => Iz = m*r² * (g/aef - 1)
#koristimo aef iz (b) prikaza (s-t2)

aef = aef_st2
daef = daef_st2

Iz = m * r**2 * (g / aef - 1)

#pogreska: dIz/daef = -m*r²*g / aef²
dIz = m * r**2 * (g / aef**2) * daef

print("\nc) Moment tromosti")
print(f"aef = {aef:.4f} ± {daef:.4f} m/s²")
print(f"Iz  = {Iz:.6e} ± {dIz:.6e} kg·m²")
