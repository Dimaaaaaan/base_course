number = int(input("Введите натуральное число: "))

devider = 2

while number > 1:
    if number % devider == 0:
        print(devider, end=' ')
        number //= devider 
    else:
        devider += 1
        