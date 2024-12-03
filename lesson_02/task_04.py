"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

import decimal
import math

decimal.getcontext().prec = 60
pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
pi_2 = decimal.Decimal(math.pi)
LIMIT_DIAMETER = 1000

diameter: int = int(input(f'Введите диаметр не превышающий {LIMIT_DIAMETER}: '))

while 0 > diameter or diameter > LIMIT_DIAMETER:
    print('Введено число не из заданного диапазона!')
    diameter: int = int(input(f'Введите диаметр не превышающий {LIMIT_DIAMETER}: '))

circuit = pi * decimal.Decimal(diameter)
circuit_2 = pi_2 * decimal.Decimal(diameter)

area = pi * (decimal.Decimal(diameter) / 2) ** 2
print('длина_1: ', circuit)
print('длина_2: ', circuit_2)
print('площадь: ', area)