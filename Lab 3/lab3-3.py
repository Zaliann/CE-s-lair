""" Срез используется для получения нескольких символов (подстроки) из строки.
Его синтаксис аналогичен синтаксису индексации, но вместо одного индекса вы используете два индекса (целых числа), разделенных двоеточием.
Например, str[2:5]
"""

monty_python = "Monty Python"

print(monty_python[1:5])

monty = monty_python[:5] 	# Один или оба индекса могут быть отброшены.
monty_python[:5] 	# Эквивалентен выражению monty_python[0:5]
print(monty)

python = monty_python[6:]		# Используйте оператор среза для получения подстроки “Python”
print(python)



# Используйте ключевое слово in для проверки того, содержится ли подстрока в строке.

ice_cream = "ice cream"

print("cream" in ice_cream) 	# Обратите внимание на результат операции

# Проверьте есть ли подстроки "ice", "Ice" и "iсe " в строке "ice cream". Выведите результаты каждой из проверок.
print('ice' in ice_cream)
print('Ice' in ice_cream)
print('ice ' in ice_cream)


# Функция len() используется для подсчета количества символов в строке

# Символы """ и """ используются для создания многострочной строки

phrase = """

It is a really long string

triple-quoted strings are used

to define multi-line strings

"""

# Получите первую половину строки, хранящейся в переменной phrase.
# Примечание: не забудьте о преобразовании типов.
first = phrase[:len(phrase) // 2 + 1]
print(first)