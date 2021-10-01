name, surname = [x for x in input('Enter your name and surname').split()]
num_of_group = int(input('Enter number of your group'))
print('Привет, ', surname + ' ' + name, ' из группы ', num_of_group, '!',sep='')
email = input('Введи свою электронную почту?')
print(surname[:5].lower(), (name[:5].lower()) * 2, (email[:5].lower()) * 3,sep='')
