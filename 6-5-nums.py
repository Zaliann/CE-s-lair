import os


def out_print(s, n):
    # данная функция печатает в документ output.txt строку, а затем число, следущее после строки
    f.write(s + ' ' + str(n) + '\n')


if  'input.txt' not in os.listdir(os.getcwd()):
    print('Файл с входными данными не обнаружен')
    exit()

f = open("input.txt", 'r')
s = f.read()
f.close()
ar = [int(x) for x in s.split()]
n = ar[0]
amount = len(str(ar[0]))
sum_n = 0
mult_n = 1
for i in range(amount):
    digit = int(str(n)[i])
    sum_n += digit
    mult_n *= digit
f = open("output.txt", 'w')
out_print('Число:', n)
out_print('Количество цифр:', amount)
out_print('Сумма цифр:', sum_n)
out_print('Произведение цифр:', mult_n)
f.close()