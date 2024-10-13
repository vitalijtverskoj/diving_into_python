from random import randint

"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Программа загадала число от {LOWER_LIMIT} до {UPPER_LIMIT}!')

for i in range(ATTEMPTS):
    print('Количество попыток:', ATTEMPTS - i)
    number = int(input('Введите число: '))
    if number < num:
        print('Число больше!')
    elif number > num:
        print('Число меньше!')
    else:
        if i == 0:
            print('Невероятно! Вы отгдадали с первого раза!!!')
            break
        print('Вы отгадали. Правильное число:', num)
        break
else:
    print('Вы проиграли. Правильное число:', num)