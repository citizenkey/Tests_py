# Компьютер загадывает случайное число от 1 до 100. Человек угадывает.

# 4 вариант, как только пользователь угадал, объявляем победителя
import random

number = random.randint(1, 100)
print(number)

user_number = None
count = 0  # вводим кол-во попыток
levels = {1: 10, 2: 5, 3: 3} # объявляем уровни сложности на 1 уровне 10, на 2 - 5, на 3 - 3

level = int (input('введите уровень сложности 1-3: '))
max_count = levels[level]

user_count = int(input('введите кол-во пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'введите имя пользователя {i}: ')
    users.append(user_name)

is_winner = False # Обозначает что есть победитель
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('')
        print('Жаль, все пользователи проиграли ')
        break
    print(f'попытка № {count}')
    for user in users:
        print(f'ход пользователя {user}')
        user_number = int(input(('введите число: ')))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('введенное число больше загаданного')
        else:
            print('введенное число меньше загаданного')
else:
    print('')
    print(f'Победитель {winner_name}')
'''
# 3 вариант многопользовательский
import random

number = random.randint(1, 100)
print(number)

user_number = None
count = 0  # вводим кол-во попыток
levels = {1: 10, 2: 5, 3: 3} # объявляем уровни сложности на 1 уровне 10, на 2 - 5, на 3 - 3

level = int (input('введите уровень сложности 1-3: '))
max_count = levels[level]

user_count = int(input('введите кол-во пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'введите имя пользователя {i}: ')
    users.append(user_name)

while number != user_number:
    count += 1
    if count > max_count:
        print('')
        print('Жаль, все пользователи проиграли ')
        break
    print(f'попытка № {count}')
    for user in users:
        print(f'ход пользователя {user}')
        user_number = int(input(('введите число: ')))
        if number < user_number:
            print('введенное число больше загаданного')
        elif number > user_number:
            print('введенное число меньше загаданного')
else:
    print('')
    print('Победа!')
'''


'''
# 2 вариант

import random

number = random.randint(1, 100)
print(number)

user_number = None
count = 0  # вводим кол-во попыток
levels = {1: 10, 2: 5, 3: 3} # объявляем уровни сложности на 1 уровне 10, на 2 - 5, на 3 - 3
level = int (input('введите уровень сложности 1-3: '))
max_count = levels[level]

while number != user_number:
    count += 1
    if count > max_count:
        print('')
        print(':Жаль, вы проиграли ')
        break
    print(f'попытка № {count}')
    # вводим число
    user_number = int(input(('введите число: ')))
    # сравниваем и выводим сообщение
    if number < user_number:
        print('введенное число больше загаданного')
    elif number > user_number:
        print('введенное число меньше загаданного')
else:
    print('')
    print('Победа!')
'''

'''
# 1 вариант
# загадываем случайное число
import random

number = random.randint(1, 100)
print(number)

while True:
    # вводим число
    user_number = int(input(('введите число_ ')))
    # сравниваем и выводим сообщение
    if number == user_number:
        print('Победа!')
        break
    elif number < user_number:
        print('введенное число больше загаданного')
    else:
        print('введенное число меньше загаданного')
'''
