"""
Задание 2. Преобразование числа в шестнадцатеричное
представление.
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.
"""

DIGIT_SYMBOL = '0123456789abcdef'

num = int(input('Введите целое число: '))

if num == 0:
    hex_num = '0x0'
else:
    is_negative = num < 0
    if is_negative:
        num = -num
    hex_num = ''
    while num:
        cur_num = num % 16
        hex_num = DIGIT_SYMBOL[cur_num] + hex_num
        num //= 16
    if is_negative:
        hex_num = '-0x' + hex_num
    else:
        hex_num = '0x' + hex_num

print('Введённое число в шестнадцатеричном виде: ', hex_num)
