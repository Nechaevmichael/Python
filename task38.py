# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))

line = 'house=дом car=машина men=человек tree=дерево'.split()
# result = []
# for l in line.split():
#   s = tuple(l.split('='))
#   result.append(s)
# print(tuple(result))

# tp = tuple(tuple(l.split('=')) for l in line.split())
# print(tp)

line = tuple(map(lambda x: tuple(x.split('=')), line))
print(line)
