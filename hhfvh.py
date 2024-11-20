import numpy as np
import matplotlib.pyplot as plt

def plot_hyperbola(x_min, x_max, N):
    # Проверка корректности входных данных

    
    # Генерация значений x в заданных пределах
    x_values = np.linspace(x_min, x_max, N)
    
    # Избегаем деления на ноль
 

    # Вычисление соответствующих значений y
    y_values = 1 / x_values

    # Построение графика
 
    plt.plot(x_values, y_values, label='Гипербола y = 1/x', color='blue')


   
    
    
    
    plt.savefig('ihfhf.png')

# Пример использования функции
plot_hyperbola(-10, 10, 1000)