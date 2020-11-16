from functools import reduce
start = 100
stop = 1000
step = 1
stop = stop + step
multiplicity = reduce(lambda x, y: x * y, [el for el in range(start, stop, step) if el % 2 == 0])
print(multiplicity)
