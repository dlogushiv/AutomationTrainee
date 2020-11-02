# 2. Получить список всех чисел Фибоначчи на отрезке [a, b].

def fibo(x):
    c = [0, 1]
    i = c[0]
    j = c[1]
    while j <= x - i:
        fib = i + j
        i, j = j, fib
        c.append(fib)
    return c


a = int(input())
b = int(input())

result = [i for i in fibo(b) if i >= a]
print(result)
