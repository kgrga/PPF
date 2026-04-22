import matplotlib.pyplot as plt
from Projectile import Projectile


p = Projectile(v0=50, angle=45, k=0.02)

dt_values = [0.5, 0.1, 0.05, 0.01]

plt.figure()

for dt in dt_values:
    traj = p.euler(dt)
    plt.plot(traj[:, 0], traj[:, 1], label=f"Euler dt={dt}")

plt.title("Zadatak 1: Euler metoda - utjecaj dt")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.grid()
plt.show()
