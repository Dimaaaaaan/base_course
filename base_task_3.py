import numpy as np

x_0 = 0
y_0 = 0
v_0 = 50.0  
g = 9.81 

t_values = np.arange(0, 5.1, 1) 

results = []

for t in t_values:
    x = x_0 + v_0  * t
    y = y_0 + v_0 * t - 0.5 * g * t**2
    results.append((t, x, y))

print("t (с)  x (м)  y (м)")
for result in results:
    print(f"{result[0]}  {result[1]}  {result[2]}")