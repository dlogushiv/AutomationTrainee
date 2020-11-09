# 1. Получить список всех нечётных чисел на отрезке [a, b].

# a = int(input())
# b = int(input())
#
# c = list(range(a, b + 1))
# result = [i for i in c if i % 2 == 1]
# print(result)


def odd(a, b):
    return [i for i in range(a, b + 1) if i % 2]


print(odd(0, 10))
