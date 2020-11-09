# 3. Напишите функцию, которая принимает на вход два параметра: a и b.
# •	если тип обоих переменных (a и b) - int, вывести большее из них
# •	если тип обоих переменных строка - сообщить, является ли строка b подстрокой строки a
# •	если переменные разного типа, вывести сообщение об ошибке (любое)

def check_inputs(a, b):
    if type(a) is int and type(b) is int:
        print('Inputs are Integer. Max is: ', end='')
        print(a if a >= b else b)
    elif type(a) is str and type(b) is str:
        if b in a:
            print('Line "' + a + '" contain line "' + b + '".')
        else:
            print('Line "' + a + '" doesn\'t contain line "' + b + '".')
    else:
        print('Inputs have different types.')


check_inputs(5, 10)
check_inputs(5, 'aaa')
check_inputs('qwerty', 'wer')
check_inputs('qwerty', 'bnv')
