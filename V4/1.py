import numpy as np
import matplotlib.pyplot as plt

# --- konstante (možeš i SI, ali ovo je stabilnije)
q_e = -1.0
q_p =  1.0
m = 1.0

# polja
E = np.array([0.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0])

# početni uvjeti
r0 = np.array([0.0, 0.0, 0.0])
v0 = np.array([1.0, 1.0, 1.0])

dt = 0.05
steps = 4000

def boris_push(q):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))

    r[0] = r0
    v[0] = v0

    for i in range(steps - 1):
        # half acceleration by E
        v_minus = v[i] + (q * E / m) * (dt / 2)

        # rotation due to B
        t = (q * B / m) * (dt / 2)
        t_mag2 = np.dot(t, t)
        s = 2 * t / (1 + t_mag2)

        v_prime = v_minus + np.cross(v_minus, t)
        v_plus = v_minus + np.cross(v_prime, s)

        # second half E
        v[i+1] = v_plus + (q * E / m) * (dt / 2)

        # update position
        r[i+1] = r[i] + v[i+1] * dt

    return r

# simulacije
traj_e = boris_push(q_e)
traj_p = boris_push(q_p)

# --- crtanje
fig = plt.figure(figsize=(10, 5))

ax = fig.add_subplot(121, projection='3d')
ax.plot(traj_e[:,0], traj_e[:,1], traj_e[:,2])
ax.set_title("Elektron")

ax = fig.add_subplot(122, projection='3d')
ax.plot(traj_p[:,0], traj_p[:,1], traj_p[:,2])
ax.set_title("Pozitron")

plt.show()