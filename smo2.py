import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

k = 1  # spring constant
m = 1  # mass
x0 = 0  # initial position
v0 = 1  # initial velocity

w = np.sqrt(k/m)  # angular frequency
A = np.sqrt(x0**2 + (v0/w)**2)  # amplitude

def update(num):
    x = A*np.cos(w*num)
    spring.set_data([0, x], [0, 0])
    mass.center = (x, 0)

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

spring, = ax.plot([], [], 'g-', lw=2)
mass = plt.Circle((x0, 0), 0.1, fc='b')
ax.add_patch(mass)

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10*np.pi, 500), blit=False)
plt.show()