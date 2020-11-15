def division(arg_1, arg_2):
    try:
        s_div = arg_1 / arg_2
        return s_div
    except ZeroDivisionError as err:
        return print('Деление на ноль', err)

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
result = division(num_1, num_2)
print(result)