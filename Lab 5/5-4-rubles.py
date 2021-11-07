'''
Данная программа печатает количество рублей и количество копеек, которые должен заплатить
покупатель.
'''

def evaluation(sump):
    """
    Данная функция подсчитывает количество рублей и копеек и выводит их на экран
    :param sump: сумма покупки в копейках
    :return:
    """
    rubles = sump // 100
    if rubles % 10 >= 5 or rubles in range(10, 21):
        print(rubles, 'РУБЛЕЙ')
    elif rubles % 10 in (2, 3, 4):
        print(rubles, 'РУБЛЯ')
    elif rubles % 10 == 1:
        print(rubles, 'РУБЛЬ')
    elif rubles > 0 and rubles % 10 == 0:
        print(rubles, 'РУБЛЕЙ')

    cents = sump % 100
    if cents % 10 >= 5 or cents in range(10, 21):
        print(cents, 'КОПЕЕК')
    elif cents % 10 in (2, 3, 4):
        print(cents, 'КОПЕЙКИ')
    elif cents % 10 == 1:
        print(cents, 'КОПЕЙКА')
    elif cents > 0 and cents % 10 == 0:
        print(cents, 'КОПЕЕК')

    return

# основная программа
sump = int(input())
evaluation(sump)