import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры анимации
g = 9.81  # ускорение свободного падения (м/с^2)
bounce_factor = 0.8  # коэффициент отскока
dt = 0.05  # шаг времени (с)

# Начальные условия
y = 10.0  # начальная высота (м)
v = 0.0   # начальная скорость (м/с)

# Инициализация фигуры для анимации
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)  # пределы по оси X
ax.set_ylim(0, 12)  # пределы по оси Y
ball, = plt.plot([], [], 'o', markersize=20, color='red')  # мяч

# Функция инициализации
def init():
    ball.set_data([], [])
    return ball,

# Функция обновления для анимации
def update(frame):
    global y, v

    # Обновление положения и скорости
    v += -g * dt  # падение под действием гравитации
    y += v * dt  # обновление позиции мяча

    # Проверка на отскок
    if y <= 0:  # если мяч касается земли
        y = 0  # коррекция позиции на уровне пола
        v = -v * bounce_factor  # смена направления и уменьшение скорости

    ball.set_data(0, y)  # обновление положения мяча
    return ball,

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=50)

plt.title("Падение мяча под действием гравитации")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
plt.savefig('task_10_Astroida')
