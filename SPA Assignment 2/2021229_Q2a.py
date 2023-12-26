import matplotlib.pyplot as plt
import numpy as np

# Parameters
p = 0.5 
num_steps = 500
start_state = 0

# Initialize array to store walk
walk = np.zeros(num_steps+1)
walk[0] = start_state

# Simulate random walk  
for i in range(1, num_steps+1):
    if np.random.rand() < p:
        walk[i] = walk[i-1] + 1
    else:
        walk[i] = walk[i-1] - 1

# Plot results        
plt.plot(walk)
plt.title("1D Random Walk")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.show()

# Calculate empirical probability distribution
values, counts = np.unique(walk, return_counts=True)
prob_dist = counts / num_steps
print(prob_dist)