# Задано N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# *'  1 2 3 4 6 7 -> 5
# *'  1 3 -> 2


n = [0, 1, 2, 4, 6, 7]
result = 0
for i in range(len(n)):
    if n[i + 1] - n[i] != 1:
        result = n[i] + 1
        break
print(result)
