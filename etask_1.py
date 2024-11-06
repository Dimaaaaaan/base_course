rows = 4
cols = 3
array1 = [[0] *
cols for - in range(rows) ]
array2 = [[0] * cols for
- in range(rows) ]
array3 = [[0] * cols for
in range(rows) ]
print ("Введите элементы первого массива (4х3):")
for i in range (rows):
for j in range (cols):
array1 (ilj] = int(input (f"array1(il ill: "))
print ("Введите элементы второго массива (4х3):")
for i in range(rows) :
for j in range(cols):
array2[1][j] = int (input(f"array2[(1)][(3)]: *))
for i in range (rows) :
for j in range(cols):
array3[1] [3] - max (array1[1][3], array2[1][j])
print("Третий массив (большие элементы) :*)
for
row in array3:
print (row)