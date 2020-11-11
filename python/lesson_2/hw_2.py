some_list = list(input('Enter some element: '))
for i in range(0, len(some_list) - 1, 2):
    some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
print(some_list)
