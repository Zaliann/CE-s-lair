'''
Данная программа печатает время прибытия поезда на конечную станцию и определяет количество полных суток
в пути до конечной станции.
'''

def time2end(hour_start, min_start, hour_way, min_way):
    """
    Данная функция выводит время прибытия и полное количество суток в пути
    :param hour_start: час отправления
    :param min_start: минуты отправления
    :param hour_way: часов в пути
    :param min_way: минут в пути
    :return:
    """

    min_overall = hour_start * 60 + min_start + hour_way * 60 + min_way
    hour_end = (min_overall // 60) % 24
    if hour_end < 10:
        print('0' + str(hour_end) + ' hours',end=' : ')
    else:
        print(str(hour_end) + ' hours', end=' : ')
    min_end = min_overall % 60
    if min_end < 10:
        print('0' + str(min_end) + ' minutes')
    else:
        print(str(min_end) + ' minutes')
    print(hour_way // 24, 'days')
    return

# основная программа
hotp = int(input())
motp = int(input())
hp = int(input())
mp = int(input())
time2end(hotp, motp, hp, mp)