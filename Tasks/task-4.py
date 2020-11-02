# 4. Напишите функцию, которая принимает на вход три параметра:
# начальный год (a),
# конечный год (b),
# список годов (c).
# функция должна вернуть список високосных лет между а і b, кроме тех которые указаны в списке c.


def leap_year(a, b, c):
    result = []
    years = list(range(a, b + 1))
    for year in years:
        if year % 4 == 0 and year not in c:
            result.append(year)
    return result


x = int(input())
y = int(input())
z = [int(i) for i in input().split()]
print(leap_year(x, y, z))
print(z)
