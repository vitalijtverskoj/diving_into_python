"""
Задание №6.
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

import decimal

CMD_DEPOSIT = '1'
CMD_WITHDRAW = '2'
CMD_EXIT = '3'
MULTIPLICITY = 50
NUMBER_OPERATION = 3
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5_000_000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)

balance = decimal.Decimal(0)
count = 0

while True:
    print_result = ''
    action = input(f'''\tБаланс карты: {balance}
    Выберите операцию:
            {CMD_DEPOSIT} - Пополнить счёт
            {CMD_WITHDRAW} - Снять деньги со счёта
            {CMD_EXIT} - Выйти
            -> ''')
    if action == CMD_EXIT:
        print(f'\nЗаберите карту. Баланс карты: {balance}')
        break
    if action in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = decimal.Decimal(input(f'Введите сумму кратную {MULTIPLICITY}: '))

        if action == CMD_DEPOSIT:
            count += 1
            balance += amount
            print_result = print_result + f'\nПополнение карты на {amount}. \nБаланс карты: {balance}\n'
        elif action == CMD_WITHDRAW:
            percent = amount * PERCENT_REMOVAL
            percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
            sub = amount + percent
            if balance > sub:
                balance -= sub
                count += 1
                print_result = print_result +  (f'\nСнятие с карты {amount} у.е. \nСумма процента за снятие {percent}.'
                                                f'\nБаланс карты {balance}\n')
            else:
                print_result = print_result + (f'\nНедостаточно средств. Сумма снятия {amount}. \nСумма процента за '
                                               f'снятие {percent}.\nБаланс карты {balance}\n')
    if balance > RICHNESS_SUM:
        percent = balance * RICHNESS_PERCENT
        balance -= percent
        print_result = (f'\nВычтен налог на богатство {RICHNESS_PERCENT * 100}%.'
                        f'\nСумма процента - {percent}. \nБаланс карты - {balance}\n')
    if count % 3 == 0:
        bonus = balance * PERCENT_BONUS
        balance += bonus
        print_result = print_result + (f'\nНачислен бонус: {bonus} за каждую {NUMBER_OPERATION} операцию.'
                        f'\nБаланс карты {balance}\n')
    print(print_result)
# count = 0
# quantity = 0
#
# while True:
#     count = round(count, 2)
#     if count > 5_000_000:
#         print(f'Вычет налога на богатство в размере: {count * 0.10}')
#         count -= count * 0.10
#     if quantity == 3:
#         print(f'Начислены проценты: {count * 0.03}')
#         count += count * 0.03
#         quantity = 0
#     print('Сумма счёта: ', count)
#     _ = input('''Выберите операцию:
#     1 - Пополнить счёт
#     2 - Снять деньги со счёта
#     3 - Выйти
#     -> ''')
#     if _ == '1':
#         print('Сумма счёта: ', count)
#         add_sum = input('Введите сумму денег кратную 50 у.е: ')
#         while not add_sum.isdigit() or int(add_sum) % 50 != 0:
#             print('Вы ввели некорректную сумму!!!')
#             add_sum = input('Введите сумму денег кратную 50 у.е: ')
#         count += int(add_sum)
#         quantity += 1
#     elif _ == '2':
#         print('Сумма счёта: ', count)
#         dec_sum = input('Укажите сумму денег кратную 50 у.е для снятия: ')
#         while not dec_sum.isdigit() or int(dec_sum) % 50 != 0:
#             print('Вы ввели некорректную сумму!!!')
#             dec_sum = input('Укажите сумму денег кратную 50 у.е для снятия: ')
#         dec_sum = int(dec_sum)
#         percent = dec_sum * 0.015
#         if percent < 30:
#             percent = 30
#         elif percent > 600:
#             percent = 600
#         percent = percent + dec_sum
#         if percent < count:
#             count -= percent
#             quantity += 1
#         else:
#             print('На счету недостаточно средств!')
#     elif _ == '3':
#         print('Сумма счёта: ', count)
#         print('Завершение программы.')
#         break
