# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


n = [7, 5, 2, 3, 4, 6, 1, 7]

result = []
for i in range(len(n)):
    for j in range(i, len(n)):
        print(i, j)
        if n[j] > n[i]:
            result.append(n[j])
    if len(result) > 1:
        break
    else:
        result = []
print(result)