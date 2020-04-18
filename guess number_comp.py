# В этой игре человек загадывает число, а компьютер пытается его угадать.


# 2 вариант
import random

min_num = 1
max_num = 100
result = None

while result != "=":
    number = random.randint(min_num, max_num)
    print(number)
    result = input('Я угадал? введи знак "=", твое число больше или меньше, введи "+", "-": ')
    if result == "+":
        print('загаданное число больше')
        min_num = number + 1
    elif result == "-":
        print('загаданное число меньше')
        max_num = number - 1
print('Победа!')
'''
# 1 вариант
import random

min_num = 1
max_num = 100

while True:
    number = random.randint(min_num, max_num)
    print(number)
    result = input('Я угадал? введи знак "=", твое число больше или меньше, введи "+", "-": ')
    if result == "=":
        print('Победа!')
        break
    elif result == "+":
        print('загаданное число больше')
        min_num = number + 1
    elif result == "-":
        print('загаданное число меньше')
        max_num = number - 1
'''
