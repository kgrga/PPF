import numpy as np

class Projectile:
    def __init__(self,theta, v0, Cd, mass, A, rho, x0=0, y0=0):
        self.theta = np.radians(theta)
        self.v0 = v0
        self.Cd = Cd
        self.mass = mass
        self.A = A
        self.rho = rho
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81


    def equations(self, state):
        """Vraća derivacije koordinata i brzina za trenutno stanje."""
        x, y, vx, vy = state
        v = np.sqrt(vx**2 + vy**2)

        drag_factor = (0.5 * self.Cd * self.rho * self.A) / self.mass

        dvx = -drag_factor * v * vx
        dvy = -self.g - drag_factor * v * vy

        return np.array([vx, vy, dvx, dvy])


    def plot(self, dt=0.005):
        """
        Simulira gibanje jednog projektila.
        U petlji provjerava je li projektil u zraku (y >= 0) koristeći RK4.
        Vraća cijelu trajektoriju leta.
        """
        # Postavljanje početnog stanja
        state = np.array([self.x0, self.y0, self.v0 * np.cos(self.theta), self.v0 * np.sin(self.theta)])
        trajectory = []

        # Petlja provjerava je li projektil još uvijek u zraku
        while state[1] >= 0:
            trajectory.append(state.copy())

            # Runge-Kutta 4. reda
            k1 = self.equations(state)
            k2 = self.equations(state + (dt / 2) * k1)
            k3 = self.equations(state + (dt / 2) * k2)
            k4 = self.equations(state + dt * k3)
            
            state = state + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        return np.array(trajectory)