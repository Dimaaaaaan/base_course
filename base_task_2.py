b1 = int(input('Введите первый член геометрической прогрессии: '))
q = int(input('Введите знаменатель геометрической прогрессии: '))
n = int(input('Введите количество членов геометрической прогресии:'))

for i in range(n):
    geometric_progression = b1 * (q ** i)
    print(f'Член {i + 1}: {geometric_progression}')