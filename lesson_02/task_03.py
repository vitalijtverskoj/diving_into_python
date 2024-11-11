"""
Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления.
✔ Избегайте магических чисел.
✔ Добавьте аннотацию типов, где это возможно
"""

BIN: int = 2
OCT: int = 8

num: int = int(input('Введите целое число: '))

for div in BIN, OCT:
    test_num: int = num
    res: str = ''
    while test_num:
        cur_num = test_num % div
        res = str(cur_num) + res
        test_num //= div
    print(f'для {div} {res=}')

# def change_notation(number: int, sys: int) -> str:
#     res: str = ''
#     while number:
#         digit: str = str(number % sys)
#         res = digit + res
#         number //= sys
#     return res
#
# print('Бинарное представление числа: ', change_notation(num, BIN))
# print('Восьмеричное представление числа: ', change_notation(num, OCT))