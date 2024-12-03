"""
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""


LOW_LIMIT_NUM = 1
UPPER_LIMIT_NUM = 999
TEN = 10
HUNDRED = 100

# num = LOW_LIMIT_NUM
# while num <= LOW_LIMIT_NUM or num >= UPPER_LIMIT_NUM:
#     num = int(input(f'Введите число от {LOW_LIMIT_NUM} до {UPPER_LIMIT_NUM}: '))

while True:
    num = int(input(f'Введите число от {LOW_LIMIT_NUM} до {UPPER_LIMIT_NUM}: '))
    if LOW_LIMIT_NUM <= num <= UPPER_LIMIT_NUM:
        break

if num < TEN:
    result = f'Квадрат числа {num} равно: {num*num}'
elif HUNDRED > num:
    first_digit = num % TEN
    second_digit = num // TEN
    result = f'Произведение цифр числа {num} равно: {first_digit * second_digit}'
else:
    first_digit = num % TEN
    second_digit = num // TEN % TEN
    third_digit = num // HUNDRED
    result = f'Зеркальное отображение числа {num} равно: {first_digit * HUNDRED + second_digit * TEN + third_digit}'
print(result)