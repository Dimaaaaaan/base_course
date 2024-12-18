import numpy as np
import matplotlib.pyplot as plt

# Параметры
R = 1  # радиус

# Параметр t
t_cycloid = np.linspace(0, 2 * np.pi, 1000)
t_astroide = np.linspace(0, 2 * np.pi, 1000)

# Циклоида
x_cycloid = R * (t_cycloid - np.sin(t_cycloid))
y_cycloid = R * (1 - np.cos(t_cycloid))

# Астроида
x_astroide = R * (t_astroide - (1/4) * np.sin(4 * t_astroide))
y_astroide = R * (1 - (1/4) * np.cos(4 * t_astroide))

# Построение графиков
plt.figure(figsize=(12, 6))

# Циклоида
plt.subplot(1, 2, 1)
plt.plot(x_cycloid, y_cycloid, label='Циклоида', color='blue')
plt.title('Циклоида')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid()
plt.legend()

# Астроида
plt.subplot(1, 2, 2)
plt.plot(x_astroide, y_astroide, label='Астроида', color='orange')
plt.title('Астроида')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()