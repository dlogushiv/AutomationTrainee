# 8 Посчитать количество элементов больше нуля.

a = [6, -8, 1, -20, 48, 3, -1, -0, -8, 15]
result = 0
for el in a:
    if el < 0:
        result += 1
print(result)
