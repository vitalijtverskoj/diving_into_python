"""
Задача 4. Сумма и произведение дробей
Программа принимает две строки вида "a/b" - дробь с числителем и
знаменателем. Возвращает сумму и произведение дробей. Для проверки
используется модуль fractions.
"""

fractions_01 = input('Введите первую дробь вида a/b: ')
fractions_02 = input('Введите вторую дробь вида c/d: ')

a, b = map(int, fractions_01.split('/'))
c, d = map(int, fractions_02.split('/'))

sum_fractions = f'{(c * b) + (a * d)}/{b * d}'
product_fractions = f'{c * a}/{b * d}'

print('Сумма дробей: ', sum_fractions)
print('Произведение дробей: ', product_fractions)
