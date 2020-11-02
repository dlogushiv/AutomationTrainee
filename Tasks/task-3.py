# 3. Напишите функцию, которая принимает на вход два параметра: a и b.
# •	если тип обоих переменных (a и b) - int, вывести большее из них
# •	если тип обоих переменных строка - сообщить, является ли строка b подстрокой строки a
# •	если переменные разного типа, вывести сообщение об ошибке (любое)

def check_inputs(a, b):
    if a.isnumeric() and b.isnumeric():
        print('Inputs are Integer. Max is: ', end='')
        print(a) if int(a) >= int(b) else print(b)
    elif a.isdigit() or b.isdigit():
        print('Inputs have different types.')
    else:
        if a.find(b) != -1:
            print('Line "' + a + '" contain line "' + b + '".')
        else:
            print('Line "' + a + '" doesn\'t contain line "' + b + '".')


x = input()
y = input()
check_inputs(x, y)
