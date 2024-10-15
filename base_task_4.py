number = int(input('Введите число элементов ряда Фибоначчи: '))
number_1 = 1
number_2 = 1

for _ in range(number):
    print(number_1 , end=' ')
    number_1, number_2 = number_2, number_1 + number_2
