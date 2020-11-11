some_list = input('Please enter some text: ').split()
for number, item in enumerate(some_list, 1):
    print(number, item[:10])
