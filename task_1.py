import random

N = int(input('Введите длину массива: '))
array1 = [random.randint(0,100) for i in range(N)]
array2 = [random.randint(0,100) for j in range(N)]
array3 = [random.randint(0,100) for k in range(N)]

max_element = max(array1 + array2 + array3)
total_sum = sum(array1) + sum(array2) + sum(array3)

print(array1)
print(array2)
print(array3)
print(max_element)
print(total_sum)