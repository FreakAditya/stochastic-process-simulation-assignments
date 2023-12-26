import numpy as np

P = np.array([[0.5, 0.3, 0, 0.2],
              [0.2, 0.5, 0.1, 0.2],
              [0.1, 0.3, 0.3, 0.3],
              [0, 0.2, 0.3, 0.5]])

P20 = np.linalg.matrix_power(P, 20)
print("Markov chain after 20 min :")
print(P20)
print("P(X20 = s | X0 = r) =", P20[0][3])

