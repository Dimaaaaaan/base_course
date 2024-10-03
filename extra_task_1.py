coef_a = int(input("Введите коэффициент a: "))
coef_b = int(input("Введите коэффициент b: "))
coef_c = int(input("Введите коэффициент c: "))

print(f'Квадратное уравнение:  {coef_a} * x**2 + {coef_b} * x + {coef_c}')

D = coef_b ** 2 - 4 * coef_a * coef_c

x1 = (-coef_b + D**0.5) / (2 * coef_a)

x2 = (-coef_b - D**0.5) / (2 * coef_a)

if D > 0:
    print('Уравнение имеет два корня')
    print(f'Корни ураввнения: {x1} и {x2}')
elif D == 0:
    print("Уравнение имеет один корень")
    print(f'Корень уравнения: {x1}')
elif D < 0:
    print("Уравненние не имеет корней")
