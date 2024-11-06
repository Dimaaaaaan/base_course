import base_task_4 as bs4
import numpy as np

column_1 = int(input('Один столбец: ')) - 1
column_2 = int(input('Другой столбец:')) - 1


mtx = np.zeros((bs4.N, bs4.M))

mtx[:, column_1], mtx[:][column_2] = bs4.mtx[:, column_2], bs4.mtx[:][column_1]
print(mtx)