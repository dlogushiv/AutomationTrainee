# 12 Из двух отсортированных массивов сделать третий отсортированный, не сортируя его.

a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8, 10, 12, 14]

c = []
i = j = 0
while i < len(a) or j < len(b):
    if i > len(a) - 1:
        c.append(b[j])
        j += 1
    elif j > len(b) - 1:
        c.append(a[i])
        i += 1
    elif a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
print(c)
