import numpy as np

P = np.array([[0.5, 0.3, 0, 0.2],
              [0.2, 0.5, 0.1, 0.2],
              [0.1, 0.3, 0.3, 0.3],
              [0, 0.2, 0.3, 0.5]])


P25 = np.linalg.matrix_power(P, 10000)
print()
print("Markov chain after 25 min :")
print(P25)

# Compute P^5
P5 = np.linalg.matrix_power(P, 5)

# Print P(X25 = s | X20 = s)
print("P(X25 = s | X20 = s): ", P5[3][3])
