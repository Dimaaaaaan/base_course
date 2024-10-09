side1 = int(input('Введите длину первой стороны: '))
side2 = int(input('Введите длину второй стороны: '))
side3 = int(input('Введите длину третьей стороны: '))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('Такой треугольник существует.')

    if side1 == side2 == side3:
        print('Треугольник равносторонний.')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Треугольник равнобедренный.')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника не существует')