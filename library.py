# Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Вывести дату в текстовом виде,
# например: второе ноября 2013 года. Склонением пренебречь.
data = '02.11.2013'
d, m, y = data.split('.')
print(d, m, y)  # дата состоит из 3 частей
months = {
    '02': 'февраля',
    '11': 'ноября'
}
days = {
    '02': 'второе'
}
result = f'{days[d]} {months[m]} {y} года.'
print(result)