import numpy as np
import matplotlib.pyplot as plt

b = 0.2
k = 1
phi = np.linspace(-2, 8 * np.pi, 1000)

r_log_spiral = np.exp(b * phi)
x_log = r_log_spiral * np.cos(phi)
y_log = r_log_spiral * np.sin(phi)

r_archimedean_spiral = k * phi
x_archimedean = r_archimedean_spiral * np.cos(phi)
y_archimedean = r_archimedean_spiral * np.sin(phi)

phi_jewel = np.linspace(0.01, 8 * np.pi, 1000)
r_jewel_spiral = k / np.sqrt(phi_jewel)
x_jewel = r_jewel_spiral * np.cos(phi_jewel)
y_jewel = r_jewel_spiral * np.sin(phi_jewel)

k_rose = 20
r_rose = np.sin(k_rose * phi)
x_rose = r_rose * np.cos(phi)
y_rose = r_rose * np.sin(phi)

plt.plot(x_log, y_log)
plt.title('Логарифмическая спираль')
plt.axis('equal')
plt.savefig('task4_log.png')
plt.close()

plt.plot(x_archimedean, y_archimedean)
plt.title('Архимедова спираль')
plt.axis('equal')
plt.savefig('task4_archimedean.png')
plt.close()

plt.plot(x_jewel, y_jewel)
plt.title('Спираль «жезл»')
plt.axis('equal')
plt.savefig('task4_jewel.png')
plt.close()

plt.plot(x_rose, y_rose)
plt.title('Роза')
plt.axis('equal')
plt.savefig('task4_rose.png')
plt.close()