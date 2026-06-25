import numpy as np
import matplotlib.pyplot as plt
from projectile import Projectile  

# Definiramo fiksne vrijednosti
bazna_povrsina = 0.05
bazna_gustoca = 1.2

plt.figure(figsize=(14, 6))

# =============================================================================
# Graf 1: Putanje za 4 različita koeficijenta otpora Cd
# =============================================================================
plt.subplot(1, 2, 1)

p_aero   = Projectile(mass=5.0, Cd=0.04, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)
p_sfera  = Projectile(mass=5.0, Cd=0.47, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)
p_stozac = Projectile(mass=5.0, Cd=0.50, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)
p_kocka  = Projectile(mass=5.0, Cd=1.05, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)

# Pokretanje RK4 simulacije za svaki objekt
t_aero   = p_aero.plot()
t_sfera  = p_sfera.plot()
t_stozac = p_stozac.plot()
t_kocka  = p_kocka.plot()

# Crtanje 4 krivulje
plt.plot(t_aero[:, 0], t_aero[:, 1], 'g-', linewidth=2, label=f'Aerodinamično (Cd=0.04) -> {t_aero[-1, 0]:.3f}m')
plt.plot(t_sfera[:, 0], t_sfera[:, 1], 'b-', linewidth=2, label=f'Sfera (Cd=0.47) -> {t_sfera[-1, 0]:.3f}m')
plt.plot(t_stozac[:, 0], t_stozac[:, 1], 'm-', linewidth=2, label=f'Stožac (Cd=0.50) -> {t_stozac[-1, 0]:.3f}m')
plt.plot(t_kocka[:, 0], t_kocka[:, 1], 'r-', linewidth=2, label=f'Kocka (Cd=1.05) -> {t_kocka[-1, 0]:.3f}m')

plt.title('Putanje projektila za različite koeficijente trenja ($C_d$)')
plt.xlabel('x - Udaljenost (m)')
plt.ylabel('y - Visina (m)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()


# =============================================================================
# Graf 2: Putanje za 4 različite mase
# =============================================================================
plt.subplot(1, 2, 2)

p_m05 = Projectile(mass=0.5,  Cd=0.47, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)
p_m1  = Projectile(mass=1.0,  Cd=0.47, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)
p_m5  = Projectile(mass=5.0,  Cd=0.47, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)
p_m10 = Projectile(mass=10.0, Cd=0.47, v0=10, theta=45, A=bazna_povrsina, rho=bazna_gustoca)

# Pokretanje RK4 simulacije
t_m05 = p_m05.plot()
t_m1  = p_m1.plot()
t_m5  = p_m5.plot()
t_m10 = p_m10.plot()

# Crtanje 4 krivulje
plt.plot(t_m05[:, 0], t_m05[:, 1], 'c--', linewidth=2, label=f'm = 0.5 kg -> {t_m05[-1, 0]:.3f}m')
plt.plot(t_m1[:, 0], t_m1[:, 1], 'r--', linewidth=2, label=f'm = 1.0 kg -> {t_m1[-1, 0]:.3f}m')
plt.plot(t_m5[:, 0], t_m5[:, 1], 'b--', linewidth=2, label=f'm = 5.0 kg -> {t_m5[-1, 0]:.3f}m')
plt.plot(t_m10[:, 0], t_m10[:, 1], 'g--', linewidth=2, label=f'm = 10.0 kg -> {t_m10[-1, 0]:.3f}m')

plt.title('Putanje projektila za različite mase ($m$)')
plt.xlabel('x - Udaljenost (m)')
plt.ylabel('y - Visina (m)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()