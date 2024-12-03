"""
Работа в консоли в режиме интерпретатора Python.
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""

n = int(input('Введите число n: '))
e = int(input('Введите число e: '))
sum_even = 0
i = 0
# if n%2 != 0:
#     n -= 1
#
# while n >= 0:
#     if n%e == 0:
#         n -= 2
#         continue
#     sum_even += n
#     n -= 2

while i < n:
    i += 2
    if i%e != 0:
        sum_even += i

print(f"Cумма чётных элементов равна {sum_even}")