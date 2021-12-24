from datetime import datetime
from prettytable import PrettyTable
import random
import sorts

n = int(input("Введите число элементов последовательностей: "))
list = []
for i in range(n):
    list.append(random.randint(-200000, 200000))


def time_of_sorts(list):
    # Данная функция считает время выполнения разных сортировок
    start = datetime.now().timestamp()
    sorts.bubble(list)
    b = str(datetime.now().timestamp() - start)

    start = datetime.now().timestamp()
    sorts.shell_method(list)
    s = str(datetime.now().timestamp() - start)

    start = datetime.now().timestamp()
    sorts.fast(list)
    f = str(datetime.now().timestamp() - start)

    list_c = list.copy()
    start = datetime.now().timestamp()
    list_c.sort()
    c = datetime.now().timestamp() - start

    return b, s, f, c


b1, s1, f1, c1 = time_of_sorts(list)  # случайная
list.sort()
b2, s2, f2, c2 = time_of_sorts(list)  # отсортированная
list.reverse()
b3, s3, f3, c3 = time_of_sorts(list)  # отсортированная в обратном порядке

# заполняем таблицу
table = PrettyTable()
table.add_column("Метод", ["Метод пузырька", "Метод Шелла", "Быстрая сортировка", "Встроенная функция"])
table.add_column("Случайная", [b1, s1, f1, c1])
table.add_column("Отсортированная", [b2, s2, f2, c2])
table.add_column("Отсортированная в обратном порядке", [b3, s3, f3, c3])

# переносим данные в файл
f = open("output.txt", "w")
table_txt = table.get_string()
f.write(str(sorts.check(list)) + '\n')
f.write("Число элементов последовательностей: " + str(n) + '\n')
f.write(table_txt)
f.close()