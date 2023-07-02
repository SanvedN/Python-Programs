import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial values
position = 15.0
velocity = 0.0
acceleration = 0.0

# Define the constants
mass_constant = 1.0  # mass
k = 2.5  # spring coefficient
b = 0  # damping coefficient

# Define the time step
dt = 0.05  # ΔT (sampling period) in seconds

# Define the simulation time
simulation_time = 30.0

# Callback function
def set(arg):
    global position, velocity, acceleration

    spring_force = k * position
    damper_force = b * velocity

    acceleration = -(spring_force + damper_force) / mass_constant
    velocity += acceleration * dt
    position += velocity * dt

    return (position, 0)

# Create empty lists to store position and time values
positions = []
times = []

# Animation update function
def update(frame):
    # Calculate position and time
    t = frame * dt
    positions.append(position)
    times.append(t)

    # Update the spring-mass system
    set((position, 0, velocity, 0, acceleration, 0))

    # Update the animation
    spring.set_data([0, 0], [0, -position])
    mass.set_center((0, -position))
    line.set_data(times, positions)

# Create the figure and axes for animation and graph
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Set up the animation plot
ax1.set_xlim(-1, 1)
ax1.set_ylim(-20, 20)
ax1.set_aspect('equal')
spring, = ax1.plot([0, 0], [0, -position], lw=2, color='k')
mass = plt.Circle((0, -position), 0.5, color='b') # type: ignore
ax1.add_patch(mass)

# Set up the position vs. time graph plot
ax2.set_xlim(0, simulation_time)
ax2.set_ylim(-20, 20)
line, = ax2.plot([], [], lw=2, color='r')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Position (m)')

# Create the animation
num_frames = int(simulation_time / dt)
anim = FuncAnimation(fig, update, frames=num_frames, interval=50)

# Display the plot
plt.tight_layout()
plt.show()
