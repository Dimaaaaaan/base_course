import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_steps = 10
step_height = 1
step_width = 2
bounce_factor = 1




ball_radius = 0.2
ball_x = step_width / 2 
ball_y = num_steps * step_height + ball_radius 
velocity_y = 0  
gravity = -0.01  

fig, ax = plt.subplots()
ax.set_xlim(-1, num_steps * step_width + 1)
ax.set_ylim(0, num_steps * step_height + 3)



#Мяч
ball = plt.Circle((ball_x, ball_y), ball_radius, color='red')
ax.add_artist(ball)


def update(frame):
    global ball_y, velocity_y, ball_x


    
    velocity_y  += gravity 
    ball_y += velocity_y 




    

   
    ball.set_center((ball_x, ball_y))
    return ball,


ani = animation.FuncAnimation(fig, update, frames=300, interval=20)

plt.title("Анимация мяча, падающего на лестницу")
plt.xlabel("Ширина")
plt.ylabel("Высота")
plt.grid()
plt.gca().set_aspect('equal', adjustable='box') 
plt.show()
ani.save('animation_7.gif')
