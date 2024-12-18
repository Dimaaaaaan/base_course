# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# alpha = 1  
# frames = 100

# fig, ax = plt.subplots()
# ax.set_xlim(0, np.pi * 2)
# ax.set_ylim(0, np.pi * 2)

# circle = plt.Circle((0, 0), 0)
# ax.add_artist(circle)


# def update(frame):
#     t = frame / 10 
#     r = alpha * t  
#     circle.set_radius(r)  
#     return circle


# ani = FuncAnimation(fig, update, frames=frames, blit=True)


# ani.save('task_2.gif')


	
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_move(R):
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y
 
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')
 
 
def animate(r):
    ball.set_data(circle_move(R=r*0.03))
    return ball
 
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('t2.gif', writer="pillow")