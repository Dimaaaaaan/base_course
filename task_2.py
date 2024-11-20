import matplotlib.pyplot as plt
import numpy as np


def giperbola_plotter(x1,x2,N):
    x = np.linspace(x1,x2,N)
    x != 1
    y = 1/x
    plt.plot(x,y, color = 'r')
    plt.savefig('task_2.png')

if __name__ == '__main__':
    giperbola_plotter(-10,10,1000)



