numder_1 = int(input("Введите первое число: "))
numder_2 = int(input("Введите второе число: "))

if numder_2 == 0:
    print("На ноль делить нельзя")
elif numder_1 % numder_2 == 0:
    print("Первое число делится на второе ")
    print("Частное: ", numder_1 // numder_2)
elif numder_1 % numder_2 != 0:
    print("Первое число не делится на второе")
    print("Частное: ", numder_1 // numder_2 , "; Остаток: ", numder_1 % numder_2)