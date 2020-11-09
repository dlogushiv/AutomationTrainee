# 11 Вывести элементы одного массива, которые не равны элементам второго массива.

a = [1, 2, 3, 4, 5, 6]
# b = [4, 5, 6, 7, 8, 9]
b = [2, 4, 6, 8]
# a = [2, 2, 2, 2, 2, 2, 2, 2]
# b = [1, 1, 1, 1]

# result = []
# for el in a:
#     if el not in b:
#         result.append(el)
# print(result)

res = [i for i in a if i not in b]
print(res)
