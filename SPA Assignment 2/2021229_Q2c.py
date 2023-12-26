import matplotlib.pyplot as plt
import numpy as np

# Parameters
p = 0.8
num_steps = 500
num_sims = 1000
start_state = 0

# Initialize array to store walks
walks = np.zeros((num_sims, num_steps+1)) 

# Run simulations
for i in range(num_sims):
    walk = np.zeros(num_steps+1)
    walk[0] = start_state
    
    for j in range(1,num_steps+1):
        if np.random.rand() < p:
            walk[j] = walk[j-1] + 1
        else:
            walk[j] = walk[j-1] - 1
            
    walks[i,:] = walk
            
# Plot results  
plt.plot(walks.T) 
plt.title("1D Random Walk Simulations (p=0.8)")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.show()