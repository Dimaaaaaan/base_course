import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Задаем параметры
alpha = 0.1  # Коэффициент, определяющий скорость роста радиуса
frames = 200  # Количество кадров анимации
interval = 50  # Интервал между кадрами в миллисекундах

# Создаем массив значений параметра φ от 0 до 2π
phi = np.linspace(0, 2 * np.pi, 100)

# Определяем функцию для обновления круга на каждом кадре
def update(frame):
    plt.clf()  # Очищаем предыдущий кадр
    radius = alpha * frame  # Вычисляем радиус для текущего кадра
    x = radius * np.cos(phi)  # Координаты x круга
    y = radius * np.sin(phi)  # Координаты y круга
    plt.plot(x, y)  # Отрисовываем круг
    plt.xlim(-radius - 1, radius + 1)  # Устанавливаем пределы по оси x
    plt.ylim(-radius - 1, radius + 1)  # Устанавливаем пределы по оси y
    plt.gca().set_aspect('equal')  # Сохраняем равные масштабы по обеим осям
    plt.title(f'Radius = {radius:.2f}')  # Заголовок с текущим радиусом

# Создаем фигуру для анимации
fig = plt.figure()

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=frames, interval=interval)

# Показать анимацию
plt.show()