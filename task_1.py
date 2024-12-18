import numpy as np
import matplotlib.pyplot as plt

R = 1
t = np.linspace(0, 2 * np.pi, 1000)

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

plt.plot(x, y)
plt.savefig('task_1_Cicloida.png')
plt.close()

x = R * np.cos(t)**3
y = R * np.sin(t)**3

plt.plot(x,y)
plt.savefig('task_1_Astroida')
