import random

NUMBER_OF_FILES = 6
AMOUNT_OF_ELEMENTS = 300
AMOUNT_OF_PACKS_IN_EACH_FILE = AMOUNT_OF_ELEMENTS // 30 // 3


def create_file_with_rand(file_name, num_of_elem):
    """
    Создаёт файл с рандомными данными
    """
    f = open(file_name + '.txt', 'w')
    for i in range(num_of_elem):
        f.write(str(random.randint(-1000, 1000)) + '\n')
    f.close()


def merge(list_elem, start, mid, ending):
    """
    Вспомогательная функция для merge_sort
    """
    it_a = 0
    it_b = 0
    list_res = [0 for x in range(len(list_elem))]

    while start + it_a < mid and mid + it_b < ending:
        if list_elem[start + it_a] < list_elem[mid + it_b]:
            list_res[it_a + it_b] = list_elem[start + it_a]
            it_a += 1
        else:
            list_res[it_a + it_b] = list_elem[mid + it_b]
            it_b += 1

    while start + it_a < mid:
        list_res[it_a + it_b] = list_elem[start + it_a]
        it_a += 1

    while mid + it_b < ending:
        list_res[it_a + it_b] = list_elem[mid + it_b]
        it_b += 1

    for i in range(it_a + it_b):
        list_elem[start + i] = list_res[i]
    return list_elem


def merge_sort(list_elem):
    """
     Сортировка слиянием
    """
    length = len(list_elem)
    i = 1
    while i < length:
        for j in range(0, length - i, 2 * i):
            list_elem = merge(list_elem, j, j + i, min(j + 2 * i, length))
        i *= 2
    return list_elem


def read_elem_from_file(file_name):
    """
    Читает элементы из файла, пока не встретит пробел, служащий разделителем отсортированных последовательностей
    """
    f = open(file_name + '.txt', 'r')
    list_elem = []
    while True:
        temp = f.readline()
        if temp == '/\n':
            f.close()
            return list_elem
        list_elem.append(int(temp))


def print_list_in_file(file_name, line):
    """
    Печатает заданный массив в файл
    """
    f = open(file_name + '.txt', 'a')
    for i in line:
        f.write(str(i) + '\n')
    f.write('/\n')
    line.clear()
    f.close()
    return


def sort_file(file_name):
    """
    Осуществляет первоначальную сортировку файла с данными и распределяет отсортированные данные
    по трём файлам в необходимой для нас форме
    """
    f = open(file_name + '0' + '.txt', 'r')
    list_elem = []
    for i in range(AMOUNT_OF_ELEMENTS):
        number_of_file = min(i // 30 // AMOUNT_OF_PACKS_IN_EACH_FILE + 1, 3)
        list_elem.append(int(f.readline()))
        if len(list_elem) == 30:
            print_list_in_file(file_name + str(number_of_file), merge_sort(list_elem))
            list_elem = []


def print_elem_in_file(file_name, elem):
    """
    Печатает элемент в файл
    """
    f = open(file_name + '.txt', 'a')
    f.write(str(elem) + '\n')
    f.close()


def outer_sort(file_name, ind1, ind2, num_of_file_to_leak):  # ind = 0 or 3
    """
    Осуществляет внешнюю сортировку
    """

    f1 = open(file_name + str(ind1 + 1) + '.txt', 'r')
    f2 = open(file_name + str(ind1 + 2) + '.txt', 'r')
    f3 = open(file_name + str(ind1 + 3) + '.txt', 'r')

    t1 = f1.readline()
    t2 = f2.readline()
    t3 = f3.readline()


    while True:

        if t1 == t2 == t3 == '/\n':
            print_elem_in_file(file_name + str(ind2 + num_of_file_to_leak), '/')
            return False

        if t1 == t2 == t3 == '\n':
            print_elem_in_file(file_name + str(ind2 + num_of_file_to_leak), '/')
            return True

        list_cand = [t1, t2, t3]

        min_elem = float('inf')
        for i in range(len(list_cand)):
            print(ind1, ind2, num_of_file_to_leak, list_cand)
            if list_cand[i] != '/\n' and list_cand[i] != '\n':
                print(list_cand[i], i)
                min_elem = min(min_elem, int(list_cand[i][:-1]))

        min_elem = str(min_elem)

        if t1[:-1] == min_elem:
            print_elem_in_file(file_name + str(ind2 + num_of_file_to_leak), t1[:-1])  # 'f' + '3 + 1' = 'f4'
            t1 = f1.readline()

        if t2[:-1] == min_elem:
            print_elem_in_file(file_name + str(ind2 + num_of_file_to_leak), t2[:-1])
            t2 = f2.readline()

        if t3[:-1] == min_elem:
            print_elem_in_file(file_name + str(ind2 + num_of_file_to_leak), t3[:-1])
            t3 = f3.readline()




def main_outer_sort():
    ind1 = 0
    ind2 = 3
    while True:
        for i in range(1, 4):
            if outer_sort('f', ind1, ind2, i):
                ind1, ind2 = ind2, ind1
            if num_of_file_to_leak == 1:
                num_of_file_to_leak = 2
            elif num_of_file_to_leak == 2:
                num_of_file_to_leak = 3
            else:
                num_of_file_to_leak = 1

            if t1 == t2 == t3 == '':
                f = open(file_name + str(ind1 + 1) + '.txt', 'w')
                f.close()

                f = open(file_name + str(ind1 + 2) + '.txt', 'w')
                f.close()

                f = open(file_name + str(ind1 + 3) + '.txt', 'w')
                f.close()

            if t1 == t2 == t3 == '':
                break

        ind1, ind2 = ind2, ind1
        f1 = open('f1.txt', 'r')
        f2 = open('f2.txt', 'r')
        f4 = open('f4.txt', 'r')
        f5 = open('f5.txt', 'r')
        if (f1.readline() != '\n' or f4.readline() != '\n') and (f2.readline() == '\n' or f5.readline() == '\n'):
            return


file = 'f0'
create_file_with_rand(file, AMOUNT_OF_ELEMENTS)
sort_file('f')
main_outer_sort()
print(1)


