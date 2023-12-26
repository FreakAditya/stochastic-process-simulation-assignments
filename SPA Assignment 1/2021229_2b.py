import matplotlib.pyplot as plt
import numpy as np

# Poisson PMF
def poisson_pmf(k, lambda_):
  return np.exp(-lambda_) * (lambda_**k) / np.math.factorial(k)

# Simulate Poisson process
def simulate_poisson(lambda_, t, num_samples):
  
  arrivals = []
  
  for _ in range(num_samples):
   
    U = np.random.uniform(0, 1)
    
    k = 0
        
    while U >= np.exp(-lambda_):
      U *= np.random.uniform(0, 1)  
      k += 1
      
    arrivals.append(k)
  
  return arrivals

# Parameters  
t = 1       
num_samples = 10000

# Simulate lambda = 5
lambda_ = 5
arrivals5 = simulate_poisson(lambda_, t, num_samples)

# Distribution for lambda = 5
k_values = np.arange(0, max(arrivals5) + 1)
probabilities5 = [np.mean(arrivals5 == k) for k in k_values]

# Simulate lambda = 15
lambda_ = 15
arrivals15 = simulate_poisson(lambda_, t, num_samples)

# Distribution for lambda = 15
probabilities15 = [np.mean(arrivals15 == k) for k in k_values]

# Plot distributions
plt.plot(k_values, probabilities5, alpha=0.7, label='lambda=5')
plt.plot(k_values, probabilities15, alpha=0.7, label='lambda=15')

plt.legend()
plt.title(f'Poisson Arrival Density for t = {t} hour')  
plt.xlabel('Number of Arrivals')
plt.ylabel('Probability') 
plt.show()

print(f"Mean for lambda=5: {np.mean(arrivals5):.2f}")
print(f"Mean for lambda=15: {np.mean(arrivals15):.2f}")