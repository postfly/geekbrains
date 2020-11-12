"""
first part of the exercise
"""


def my_func(x, y):
    result = x ** y
    return result


x = int(input('Укажите действительное положительное число: '))
y = int(input('Укажите целое отрицательное число: '))
if y >= 0:
    print('Нужно отрицательное число')
    y = int(input('Укажите целое отрицательное число: '))
print(my_func(x, y))

"""
second part of the exercise
"""


def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


x = int(input('Укажите действительное положительное число: '))
y = int(input('Укажите целое отрицательное число: '))
if y >= 0:
    print('Нужно отрицательное число')
    y = int(input('Укажите целое отрицательное число: '))
print(my_func(x, y))
