import numpy as np


class Projectile:
    def __init__(self, v0, angle, k=0.1, g=9.81):
        self.v0 = v0
        self.angle = np.radians(angle)
        self.k = k
        self.g = g

    def equations(self, state):
        x, y, vx, vy = state
        v = np.sqrt(vx**2 + vy**2)

        dvx = -self.k * v * vx
        dvy = -self.g - self.k * v * vy

        return np.array([vx, vy, dvx, dvy])


    # Euler metoda

    def euler(self, dt):
        state = np.array([
            0,
            0,
            self.v0 * np.cos(self.angle),
            self.v0 * np.sin(self.angle)])

        trajectory = []

        while state[1] >= 0:
            trajectory.append(state.copy())
            state = state + dt * self.equations(state)

        return np.array(trajectory)

   
    # Runge-Kutta 4. reda
    
    def rk4(self, dt):
        state = np.array([
            0,
            0,
            self.v0 * np.cos(self.angle),
            self.v0 * np.sin(self.angle)])

        trajectory = []

        while state[1] >= 0:
            trajectory.append(state.copy())

            k1 = self.equations(state)
            k2 = self.equations(state + dt/2 * k1)
            k3 = self.equations(state + dt/2 * k2)
            k4 = self.equations(state + dt * k3)

            state = state + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

        return np.array(trajectory)
