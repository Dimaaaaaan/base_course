import matplotlib.pyplot as plt
 
x = [3, 8, 5]
y = [1, 4, 9]
 
plt.plot(x, y, color='y', label='Graf 1', marker='>', ms=5)
plt.plot(y, x, color='b', label='Graf 2', marker='o', ms=5)
 
# --- Украшательства ---
plt.xlabel('Coord: x') # Подись оси ОХ
plt.ylabel('Coord: y') # Подпись оси ОУ
plt.legend() # Вызов "легенды"
plt.title('Base') # Общая подпись графика
plt.grid() # Подключение сетки
plt.savefig('fig_2.png')