# 9 Прибавить к элементам массива их индекс.

# a = [0, 1, 2, 3, 4, 5]
# for i in range(len(a)):
#     a[i] += i
# print(a)

b = [0, 1, 2, 3, 4, 5]
res = [b[i] + i for i in range(len(b))]
print(res)
