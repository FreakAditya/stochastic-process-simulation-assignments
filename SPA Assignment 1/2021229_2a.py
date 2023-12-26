# Import libraries
import matplotlib.pyplot as plt  
import numpy as np

# Define Poisson PMF function
def poisson_pmf(k, lambda_):
  return np.exp(-lambda_) * (lambda_**k) / np.math.factorial(k)

# Function to simulate Poisson process  
def simulate_poisson(lambda_, t, num_samples):
  
  # Initialize empty list to store results
  arrivals = []
  
  # Loop to generate samples
  for _ in range(num_samples):
  
    # Generate uniform random number 
    U = np.random.uniform(0, 1) 
    
    # Initialize arrival count
    k = 0
    
    # Increment k while random number exceeds CDF
    while U >= np.exp(-lambda_):
      U *= np.random.uniform(0, 1)
      k += 1
      
    # Append final k to results
    arrivals.append(k)
  
  # Return simulated arrivals
  return arrivals

# Set parameters
lambda_ = 5  # Poisson rate
t = 1       # Time interval  
num_samples = 10000 # Number of samples

# Simulate arrivals
arrivals = simulate_poisson(lambda_, t, num_samples)

# Calculate distribution
k_values = np.arange(0, max(arrivals) + 1)
probabilities = [np.mean(arrivals == k) for k in k_values]

# Plot distribution
plt.bar(k_values, probabilities, color='blue', alpha=0.7)
plt.title(f'Poisson Arrival Density for t = {t} hour')  
plt.xlabel('Number of Arrivals')
plt.ylabel('Probability')
plt.show()

# Print mean arrivals
mean_arrivals = np.mean(arrivals)
print(f"Mean arrivals in {t} hour = {mean_arrivals:.2f}")