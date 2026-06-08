import numpy as np
import matplotlib.pyplot as plt

#tablica
kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
kut_rad = np.radians(kut_deg)

T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653,
                  0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373,
                  1.9100, 2.5460])

T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720,
                  1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840,
                  2.4473, 3.1573])


g = 9.81  # m/s²

#nominalne duljine
L_120_nom = 0.120  # m
L_240_nom = 0.240  # m


#linearizacija: T² = (4π²·l/g) · (1/cosθ)
# y = k · x; x = 1/cosθ,  y = T²
#fit kroz ishodište: k = sum(x·y) / sum(x²)
#iz k dobivamo: l = k·g / (4π²)

x = 1 / np.cos(kut_rad)  # zajednička x-os za oba skupa

def fit_kroz_ishodiste(x, y):
    k = np.sum(x * y) / np.sum(x**2)
    # Pogreška nagiba
    reziduali = y - k * x
    sigma2 = np.sum(reziduali**2) / (len(x) - 1)
    dk = np.sqrt(sigma2 / np.sum(x**2))
    return k, dk

k_120, dk_120 = fit_kroz_ishodiste(x, T_120**2)
k_240, dk_240 = fit_kroz_ishodiste(x, T_240**2)

l_fit_120 = k_120 * g / (4 * np.pi**2)
dl_fit_120 = dk_120 * g / (4 * np.pi**2)

l_fit_240 = k_240 * g / (4 * np.pi**2)
dl_fit_240 = dk_240 * g / (4 * np.pi**2)

#rel pogreska duljine njihala
rel_pogr_120 = abs(l_fit_120 - L_120_nom) / L_120_nom * 100
rel_pogr_240 = abs(l_fit_240 - L_240_nom) / L_240_nom * 100


print(f"L = 120 mm:")
print(f"Izmjerena duljina l = {l_fit_120*1000:.2f} ± {dl_fit_120*1000:.2f} mm")
print(f"Relativna pogreška  = {rel_pogr_120:.2f} %")
print(f"L = 240 mm:")
print(f"Izmjerena duljina l = {l_fit_240*1000:.2f} ± {dl_fit_240*1000:.2f} mm")
print(f"Relativna pogreška  = {rel_pogr_240:.2f} %")



def period(theta, l):
    return 2 * np.pi * np.sqrt(l / (g * np.cos(theta)))

theta_plot = np.linspace(0, np.radians(85), 300)

fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=False)
fig.suptitle('Fizikalno njihalo: period vs kut', fontsize=13)

for ax, T_mjer, L_nom, l_fit, dl_fit, rel_pogr, naziv in [
    (axes[0], T_120, L_120_nom, l_fit_120, dl_fit_120, rel_pogr_120, 'L = 120 mm'),
    (axes[1], T_240, L_240_nom, l_fit_240, dl_fit_240, rel_pogr_240, 'L = 240 mm'),
]:
    ax.scatter(kut_deg, T_mjer, color='blue', zorder=5, label='Mjerenja')
    ax.plot(np.degrees(theta_plot), period(theta_plot, L_nom), 'purple', label=f'Teorija (L_nom={L_nom*1000:.0f} mm)')
    ax.plot(np.degrees(theta_plot), period(theta_plot, l_fit), 'teal', label=f'Fit: l={l_fit*1000:.1f}±{dl_fit*1000:.1f} mm')
    ax.set_xlabel('Kut θ (°)')
    ax.set_ylabel('Period T (s)')
    ax.set_title(f'{naziv}  I  rel. pogreška = {rel_pogr:.2f} %')
    ax.legend(fontsize=8)
    ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('2.png', dpi=150)
plt.show()