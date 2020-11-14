def int_func(arg):
    result = arg.capitalize()
    return result


print(int_func('proba'))

y = input('Write the word in small letters: ').split()
d = list(map(int_func, y))
s = ' '.join(d)
print(s)
