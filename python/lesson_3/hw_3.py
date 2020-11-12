def my_func(arg_1, arg_2, arg_3):
    return sum(locals().values()) - min(locals().values())


print(my_func(50, 900, 10))
