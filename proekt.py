import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


g = 9.81
bounce_factor =1.1
dt = 0.05


x = 0.0
y = 10.0
v_y = 0.0
v_x = 2.0


fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 12)
ball, = plt.plot([], [], 'o', markersize=20, color='red')  # мяч


def init():
    ball.set_data([], [])
    return ball,


def update(frame):
    global x, y, v_x, v_y


    v_y += -g * dt
    y += v_y * dt
    x += v_x * dt


    if y >= 12.0:
        y = 12.0
        v_y = -v_y * bounce_factor


    if y <= 0:
        y = 0
        v_y = -v_y * bounce_factor


    if x >= 1.0:
        x = 1.0
        v_x = -v_x * bounce_factor
    elif x <= -1.0:
        x = -1.0
        v_x = -v_x * bounce_factor


    ball.set_data(x, y)
    return ball,


ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=50)

plt.title("Падение мяча под действием гравитации и отскок от стенок")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
ani.save('animation_7.gif')
