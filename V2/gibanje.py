from particle import Particle
import numpy as np
import matplotlib.pyplot as plt

p=Particle(10, 60)

dt_values = np.linspace(0.001, 0.1, 50)  
greske = []

a = p.analytical_range()

for dt in dt_values:
    num = p.range(dt=dt)
    rel_g = abs(num - a) / a
    greske.append(rel_g)

p.plot_trajectory()

plt.plot(dt_values, greske)
plt.xlabel("Δt")
plt.ylabel("Relativna pogreška")
plt.title("Ovisnost pogreške o vremenskom koraku")
plt.grid()
plt.show()