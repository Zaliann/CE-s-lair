'''
Данная программа определяет является ли фигура треугольником, и если да, то определяет вид треугольника
по трем заданным сторонам.
'''

def is_triangle(a, b, c):

    """
    :param a: первая сторона
    :param b: вторая сторона
    :param c: третья сторона
    :return:
    Данная функция определяет существует ли треугольник и его вид, в случае существования
    """


    first_condition = a + b > c
    second_condition = a + c > b
    third_condition = b + c > a
    if not (first_condition and second_condition and third_condition):
        print('Треугольник не существует')
    elif a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник общего вида')
    return

# основная программа
a, b, c = [int(x) for x in input().split()]
is_triangle(a, b, c)