number = int(input('Введите целое число: '))

inverted_number = 0

while number > 0:
    last_digit = number % 10
    inverted_number = inverted_number * 10 + last_digit
    number = number // 10
print(f'Перевернутое число: {inverted_number}')