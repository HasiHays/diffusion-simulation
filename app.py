import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
GRID_SIZE = 100
PARTICLE_COUNT = 5000
STEPS = 500

# Initialize grid
grid = np.zeros((GRID_SIZE, GRID_SIZE))

# Initialize particles at random positions
particles = np.random.randint(GRID_SIZE, size=(PARTICLE_COUNT, 2))

# Add particles to grid
for p in particles:
    grid[p[0], p[1]] += 1

# Function to perform the diffusion step
def diffuse():
    global particles, grid

    # Reset grid
    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    # Move each particle
    for p in particles:
        # Random walk: equal probability of moving in each direction
        direction = np.random.randint(4)
        if direction == 0:   # Up
            if p[0] > 0: p[0] -= 1
        elif direction == 1: # Down
            if p[0] < GRID_SIZE - 1: p[0] += 1
        elif direction == 2: # Left
            if p[1] > 0: p[1] -= 1
        else:                # Right
            if p[1] < GRID_SIZE - 1: p[1] += 1

        # Update grid
        grid[p[0], p[1]] += 1

# Set up plot
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='hot', interpolation='nearest')

# Update function for animation
def update(i):
    diffuse()
    im.set_array(grid)

# Run animation
ani = animation.FuncAnimation(fig, update, frames=STEPS, interval=200)
plt.show()
