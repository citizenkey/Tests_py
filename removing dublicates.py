# Даны два произвольные списка. Удалите из первого списка элементы
# присутствующие во втором списке.


a = [1, 1, 1, 3, 2, 2, 2, 4]
b = [2, 4, 5]

for number in a[:]: # Нужно организовать цикл по копии списка при помощи среза
    if number in b:
        a.remove(number)
print(a)