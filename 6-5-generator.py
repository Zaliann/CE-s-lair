import os


def creating_list_primes(n):
    # Данная функция реализует алгоритм, известный как "решето Эратосфена",
    # и возвращает список, в котором нули -- это индексы, являющиеся
    # простыми числами, а единицы -- индексы сложных чисел

    ar = [0 for x in range(n + 1)]
    for i in range(2, n + 1 + 1):
        for j in range(2, n + 1 + 1):
            if i * j < n + 1:
                ar[i * j] = 1

    return ar


def interpretation_of_list(ar):
    # Данная функция интерпретирует список, полученный применением алгоритма
    # "решето Эратосфена", и преобразует его в новый список с простыми числами
    interpretation = []
    for i in range(2, len(ar)):
        if ar[i] == 0:
            interpretation.append(i)

    return interpretation


if "input.txt" not in os.listdir(os.getcwd()):
    print('Файл с входными данными не обнаружен')
f = open("input.txt", 'r')
n = int(f.read())
f.close()
f = open("output.txt", 'w')
list_primes = interpretation_of_list(creating_list_primes(n))

for i in range(len(list_primes)):
    if i == len(list_primes) - 1:
        f.write(str(list_primes[i]) + '\n')
    else:
        f.write(str(list_primes[i]) + ' ')
f.close()
