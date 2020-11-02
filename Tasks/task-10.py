# 10 Циклический сдвиг элементов массива на k- позиций вправо.
import time

a = [0, 1, 2, 3, 4, 5]
k = 2
# a = list(range(10000000))
# k = 1000000

# циклический сдвиг на 1 элемент k-итераций -- большое время выполнения на большом количестве элементов и шаге
# start =time.time()
# j = 0
# tmp = a[len(a) - 1]
# while j != k:
#     for i in range(len(a) - 1, 0, -1):
#         a[i] = a[i - 1]
#     a[0] = tmp
#     tmp = a[len(a) - 1]
#     j += 1
# # print(a)
# stop=time.time()
# print(stop-start)
# print()

# сдвиг сразу на k элементов с заменой первых k элементов на последние k -- быстрота выполнения
# start = time.time()
j = 0
tmp = [0] * k
for i in range(len(a) - k, len(a)):
    tmp[j] = a[i]
    j += 1
for i in range(len(a) - 1, -1 + k, -1):
    a[i] = a[i - k]
for i in range(len(tmp)):
    a[i] = tmp[i]
print(a)
# print(time.time() - start)

# подсказка от жены с применением срезов
# start = time.time()
# tmp = a[len(a) - k:]
# for i in range(len(a) - 1, 0, -1):
#     a[i] = a[i - k]
# a[0:k] = tmp
# stop = time.time()
# print('Result: ', *a)
# print(stop - start)
