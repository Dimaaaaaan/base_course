import matplotlib.pyplot as plt
import numpy as np

def ellips_plotter(x_min, x_max, N):
    a = 5
    b = 3
    x = np.linspace(x_min, x_max, N)
    y_positive = b * np.sqrt(1 - (x**2) / (a**2))
    y_negative = -b * np.sqrt(1 - (x**2) / (a**2))

    plt.plot(x, y_positive, color = 'black')
    plt.plot(x, y_negative, color = 'black')
    plt.title('График эллипса')
    plt.axhline(0, color = 'black', linewidth = 0.5)
    plt.axvline(0, color = 'black', linewidth = 0.5)
    plt.legend()
    plt.savefig('task_3.png')
    plt.axis('equal')

ellips_plotter(-6, 6, 1000)