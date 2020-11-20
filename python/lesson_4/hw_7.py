def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


x = 5
for el in fact(x):
    print(el)
