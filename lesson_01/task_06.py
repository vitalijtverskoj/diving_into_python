"""
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""

REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NO_LEAP_YEAR = 100
ZERO = 0

year = int(input('Введите год в формате yyyy: '))

if year < REFORM:
    result = 'Григорианский календарь ещё не введён'
elif year % SMALL_LEAP_YEAR != ZERO or year % LARGE_NO_LEAP_YEAR == ZERO and year % BIG_LEAP_YEAR != ZERO:
    result = f'Год {year} обычный'
else:
    result = f'Год {year} високосный'

print(result)