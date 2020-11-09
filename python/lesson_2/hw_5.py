my_list = [7, 5, 3, 3, 2]
user_number = int(input('Enter a positive integer: '))
fl = False
for elem in my_list:
    if user_number > elem:
        d = my_list.index(elem)
        my_list.insert(d, user_number)
        fl = True
        break
if not fl:
    my_list.append(user_number)
    print('Вставляй в конец')
print(my_list)
