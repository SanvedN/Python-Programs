import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the spring's natural length and spring constant
L = 1
k = 1
m=1
# Define the initial position of the mass
x0 = -0.5

# Define the time step and number of frames for the animation
dt = 0.01
num_frames = 1000

# Define the function to update the position of the mass at each frame
def update(frame):
    t = frame * dt
    x = x0 * np.sin(np.sqrt(k/m) * t)
    spring.set_data([0, 0], [0, x])
    mass.center = (0, x)

# Create the figure and axes for the plot
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(1.5, -1.5)
# Create the spring and mass objects for the plot
spring, = ax.plot([0, 0], [0, x0], lw=2, color='k')
mass = plt.Circle((x0, 0), 0.05, color='b')
ax.add_patch(mass)

# Create the animation object
anim = FuncAnimation(fig, update, frames=np.arange(0, num_frames), interval=10)

plt.show()
