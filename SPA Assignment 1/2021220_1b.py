import matplotlib.pyplot as plt
import numpy as np

p = 0.5 # Probability of heads 
n = 20 # Number of coin flips
simulations = 1000 

results = []
for i in range(simulations):
    heads = 0
    for j in range(n):
        if np.random.random() < p:
            heads += 1
    results.append(heads)

plt.hist(results, bins=np.arange(n+1)-0.5) 
plt.xlabel('Number of heads')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 simulations of tossing fair coin 20 times')
plt.show()