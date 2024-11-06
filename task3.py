import numpy as np

x_0 = 0
y_0 = 0
v_0 = 50.0  
g = 9.81 
alpha = np.radians(30)

vx_0 = v_0 * np.cos(alpha)
vy_0 = v_0 * np.sin(alpha)

t = np.arange(0, 5, 0.01)
x = x_0 + vx_0 * t
y = y_0 + vy_0 * t - g * t ** 2 / 2

coord = np.zeros((len(t), 3))
coord[:, 0] = t[:]
coord[:, 1] = x[:]
coord[:, 2] = y[:]
print(coord)