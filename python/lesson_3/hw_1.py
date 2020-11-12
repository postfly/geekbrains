def division(arg_1, arg_2):
    if arg_2 == 0:
        return 'На ноль делить нельзя'
    s_div = arg_1 / arg_2
    return s_div


num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
result = division(num_1, num_2)
print(result)
