import numpy as np
import matplotlib.pyplot as plt

def simulate_spring_mass_system(mass):
    # Constants
    k = 1.0  # Spring constant
    g = 9.8  # Acceleration due to gravity
    time = np.linspace(0, 10, 1000)  # Time range for simulation

    # Initial conditions
    initial_position = 0.5
    initial_velocity = 0.0

    # Calculate angular frequency
    omega = np.sqrt(k / mass)

    # Calculate displacement and velocity using SHM equations
    displacement = initial_position * np.cos(omega * time)
    velocity = -initial_position * omega * np.sin(omega * time)

    # Calculate net force at each time step
    force_spring = -k * displacement
    force_gravity = -mass * g
    force_net = force_spring + force_gravity

    # Plot the displacement-time graph
    plt.figure(figsize=(10, 6))
    plt.plot(time, displacement, label='Displacement')
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.title('Spring-Mass System Simulation (m = {})'.format(mass))
    plt.legend()
    plt.grid(True)

    # Plot the force-time graph
    plt.figure(figsize=(10, 6))
    plt.plot(time, force_spring, label='Spring Force')
    plt.plot(time, force_gravity, label='Gravity Force')
    plt.plot(time, force_net, label='Net Force')
    plt.xlabel('Time')
    plt.ylabel('Force')
    plt.title('Force-Time Graph (m = {})'.format(mass))
    plt.legend()
    plt.grid(True)

    # Show the plots
    plt.show()

# Example usage
simulate_spring_mass_system(1.0)  # Mass of the system is 1.0 kg
