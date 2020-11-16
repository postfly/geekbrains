from itertools import count, cycle

""" Первая часть задачи """


def first_list(start):
    for el in count(start):
        yield el


now = 3
for i in first_list(now):
    if i > 10:
        break
    print(i)
print('Работа завершена')

""" Вторая часть задачи """


def second_list(go):
    for item in cycle(go):
        yield item


num = 0
old_list = [2, 5, 8, 1]
for y in second_list(old_list):
    if num > 10:
        break
    print(y)
    num += 1
print('Работа завершена')
