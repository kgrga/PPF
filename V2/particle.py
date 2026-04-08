import numpy as np
import matplotlib.pyplot as plt

g=9.81

class Particle:
    def __init__(self, v0, theta, x0=0, y0=0):
        self.v0 = v0
        self.theta = np.radians(theta)
        self.x0 = x0
        self.y0 = y0
        self.vx=v0*np.cos(self.theta)
        self.vy=v0*np.sin(self.theta)

        self.vx0=self.vx
        self.vy0=self.vy
        self.reset()


    def reset(self):
        self.x=self.x0
        self.y=self.y0

        self.vx=self.vx0
        self.vy=self.vy0    

        self.x_list=[self.x]
        self.y_list=[self.y]


    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy -= g * dt

        self.x_list.append(self.x)
        self.y_list.append(self.y)


    def range(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.move(dt)
        return self.x


    def analytical_range(self):
        return (self.v0**2 * np.sin(2*self.theta)) / g


    def plot_trajectory(self, dt=0.01):
        self.range(dt)
        plt.plot(self.x_list, self.y_list)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("Putanja projektila")
        plt.grid()
        plt.show()
