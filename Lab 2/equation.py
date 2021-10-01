x = float(input())
#y = 1 / ((1 - x ** 4 - x ** 2) ** 0,5)
#print(y)
first = x ** 4
second = x ** 2
third = 1 - first - second
forth = third ** 0.5
fifth = 1 / forth
print(fifth)