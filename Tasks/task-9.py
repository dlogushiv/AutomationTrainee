# 9 Прибавить к элементам массива их индекс.

# a = [6, -8, 1, -20, 48, 3, -1, -0, -8, 15]
a = [0, 1, 2, 3, 4, 5]
for i in range(len(a)):
    a[i] += i
print(a)
