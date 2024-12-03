"""
Задача 4. Яма
Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы:
5
5........5
54......45
543....345
5432..2345
5432112345
"""

PIT_SYMBOL = '.'

depth_pit = int(input('Введите глубину ямы: '))
width_pit = (depth_pit - 1) * 2
# num_string = ''
#
# for i in range(depth_pit):
#     num_string = num_string + f'{depth_pit - i}'
#     print(num_string, width_pit * PIT_SYMBOL, ''.join(reversed(num_string)), sep='')
#     width_pit -= 2

for i in range(depth_pit):
    for num in range(depth_pit, (depth_pit - i) - 1, -1):
        print(num, sep='', end='')
    print(width_pit * PIT_SYMBOL,sep='', end='')
    for num in range(depth_pit - i,depth_pit + 1):
        print(num, sep='', end='')
    print()
    width_pit -= 2
