"""
Задача 3. Перевод целого числа в римское число.
Программа принимает целое число и возвращает его римское представление в
виде строки.
"""

# 3567

ARABIC_NUM = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ROMAN_NUM = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

number = int(input('Введите число: '))

roman_str = ''

for i, num in enumerate(ARABIC_NUM):
    while number >= num:
        number = number - num
        roman_str = roman_str + ROMAN_NUM[i]
    if number == 0:
        break


print('Римский вариант числа: ', roman_str)