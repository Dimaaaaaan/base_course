import numpy as np
N = int (input ("Введите число строк: "))
M = int (input ("Введите число столбцов: "))

mtx = np. zeros ((N, M))
for i in range(N):
    for j in range(M):
        mtx[i,j] = (np.sin(N * (i + 1) M * (j + 1)))
        if mtx[i, j] < 0:
            mtx[i, j] = 0

print(mtx)