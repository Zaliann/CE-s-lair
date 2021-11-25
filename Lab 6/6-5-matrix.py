import numpy as np
import random


def print_matrix(file, matrix, matrix_name):
    # Данная функция печатает матрицу, её имя в заданный файл

    f = open(file, 'a')
    f.write('Матрица ' + matrix_name + '\n')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            f.write(str(matrix[i][j]) + ' ')
        f.write('\n')
    f.close()

def create_matrix(a, b):
    # Данная функция создаёт матрицу с заданными длиной и шириной, наполняя её
    # рандомными числами

    return [[random.randint(0, 50) for x in range(b)] for y in range(a)]


def mult_matrix(m1, m2):
    # Данная функция перемножает две матрицы

    return np.dot(m1, m2)

def div_on_max_elem(matrix):
    # Данная функция делит каждый элемент матрицы на наибольший элемент матрицы

    max_elem = 0
    for i in range(len(matrix)):
        max_elem = max(matrix[i])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] / max_elem

f = open("input.txt", 'r')
n, m = [int(x) for x in f.readline().split()]
k = int(f.readline().split()[-1])
f.close()
matrix1 = create_matrix(n, m)
matrix2 = create_matrix(m, k)

print_matrix('output.txt', matrix1, 'A')
print_matrix('output.txt', matrix2, 'B')

div_on_max_elem(matrix1)

matrix3 = mult_matrix(matrix1, matrix2)
print_matrix('output.txt', matrix3, 'A*B')
f.close()
