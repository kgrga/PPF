import matplotlib.pyplot as plt
from Projectile import Projectile


p = Projectile(v0=50, angle=45, k=0.02)

dt = 0.01

traj_euler = p.euler(dt)
traj_rk4 = p.rk4(dt)

plt.figure()
plt.plot(traj_euler[:, 0], traj_euler[:, 1], label="Euler")
plt.plot(traj_rk4[:, 0], traj_rk4[:, 1], '--', label="RK4")

plt.title("Zadatak 2: Euler vs RK4")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.grid()
plt.show()