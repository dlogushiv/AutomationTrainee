# 4. Напишите функцию, которая принимает на вход три параметра:
# начальный год (a),
# конечный год (b),
# список годов (c).
# функция должна вернуть список високосных лет между а і b, кроме тех которые указаны в списке c.


def leap_year(a, b, c):
    result = []
    for year in range(a, b + 1):
        if year % 4 == 0 and year not in c and (year % 400 == 0 or not year % 100 == 0):
            result.append(year)
    return result


x = int(input())
y = int(input())
z = [int(i) for i in input().split()]
print(leap_year(x, y, z))
print(z)
