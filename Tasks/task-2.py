# 2. Получить список всех чисел Фибоначчи на отрезке [a, b].

# def fibo(x):
#     c = [0, 1]
#     i = c[0]
#     j = c[1]
#     while j <= x - i:
#         fib = i + j
#         i, j = j, fib
#         c.append(fib)
#     return c
#
#
# a = int(input())
# b = int(input())
#
# result = [i for i in fibo(b) if i >= a]
# print(result)


def fibo(start, stop):
    res = []
    i = 0
    j = 1
    while i <= stop:
        if i >= start:
            res.append(i)
        i, j = j, i + j
    return res


print(fibo(10, 100))
