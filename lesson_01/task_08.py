"""
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********

"""
SPACE_SYMBOL = ' '
STAR_SYMBOL = '*'

rows = int(input('Сколько рядов у ёлки? '))
index = 1

# spaces = rows - 1
# stars = 1
#
# for i in range(rows):
#     print((spaces * SPACE_SYMBOL) + (stars * STAR_SYMBOL) + (spaces * SPACE_SYMBOL))
#     stars += 2
#     spaces -= 1

while index <= rows:
    print(SPACE_SYMBOL * (rows - index), (index * 2 - 1) * STAR_SYMBOL, SPACE_SYMBOL * (rows - index), sep='')
    index += 1
