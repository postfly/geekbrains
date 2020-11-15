def user_sum():
    total = 0
    working = True
    while working:
        numbers = input('Enter some numbers or q to exit: ')
        for num in numbers.split():
            if num == 'q':
                working = False
                break
            total += float(num)
    return total


print(user_sum())
