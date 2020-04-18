#
n = [1, 1, 3, 4, 3, 5, 6, 8, 9, 5, 2, 22]

result = []
for num in n:
    if n.count(num) == 1: #если число входит 1 раз, запишем его в список
        result.append(num)
print(result)