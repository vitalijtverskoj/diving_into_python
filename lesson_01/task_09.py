"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
"""

# first_num = 2
# last_num = 6
# index = 2
#
# for line in range(18):
#     if line == 9:
#         print()
#         index = 2
#         first_num = 6
#         last_num = 10
#
#     for col in range(first_num, last_num):
#         if (col * index) < 10:
#             print(f'{col} X {index} =  {col * index}    ', end="")
#         elif index == 10:
#             print(f'{col} X {index}= {col * index}    ', end="")
#         else:
#             print(f'{col} X {index} = {col * index}    ', end="")
#     print()
#     index += 1

LOW_LIMIT = 2
UP_LIMIT = 10
COLUMN = 4

for row in (LOW_LIMIT, LOW_LIMIT + COLUMN):
    for num_2 in range(LOW_LIMIT, UP_LIMIT + 1):
        for num_1 in range(row, row + COLUMN):
            print(f'{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}',end="\t")
        print()
    print()