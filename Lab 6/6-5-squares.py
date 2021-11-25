def PrintRectangle(a, b, file):
    # Данная функция печатает прямоугольник с заданными сторонами
    # в файл с именем  file
    f = open(file[1 : len(file) - 1], 'a')
    for i in range(b):
        if i == 0 or i == b - 1:
            f.write('* ' * a)
            f.write('\n')
        else:
            f.write('*' + ' ' * (a - 1 + a - 2) + '*')
            f.write('\n')

    f.close()

def PrintSquare(a, file):
    # Данная функция печатает квадрат с заданными сторонами
    # в файл с именем  file
    PrintRectangle(a, a, file)

# Основная программа
str = input()
file = input()
if ' ' in str:
    a, b = [int(x) for x in str.split()]
    PrintRectangle(a, b, file)
else:
    a = int(str)
    PrintSquare(a, file)