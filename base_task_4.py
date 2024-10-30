import numpy as np
N = 5
M = 10

trigonometry_array = np.zeros((N,M))
for i in N:
    for j in M:
        trigonometry_array[i, j] = np.sin(N · i + M · j + 1)