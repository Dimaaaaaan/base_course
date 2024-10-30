import numpy as np
h = 100
g = 9.80665
a = np.radians(45)
b = np.radians(35)
v = np.sqrt((g * h * np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))
print(f'Скорость v = {v} м/с')

from numpy import sqrt 
from numpy import pi
T = 200
E = 300
e = 2.7182818284590
h = 6.62607015e-34
k = 1.380649e-23 
N = (2/sqrt(pi)) * (h/(k * T) ** 3/2) * (e ** -E/(k *T)) * (E ** (T/2))
print(N)