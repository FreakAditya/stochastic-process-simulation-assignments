import matplotlib.pyplot as plt
import numpy as np

# Set arrival rate  
lam = 5 

# Simulate inter-arrival times
inter_times = np.random.exponential(scale=1/lam, size=10000)

# Plot histogram 
plt.hist(inter_times, bins=50, density=True)

# Add exponential curve 
x = np.linspace(0, max(inter_times), 100)
y = lam * np.exp(-lam*x)
plt.plot(x, y)

plt.title("Distribution of First Inter-arrival Time")
plt.xlabel("Time")
plt.ylabel("Probability")

print("Mean time:", np.mean(inter_times)) 

plt.show()