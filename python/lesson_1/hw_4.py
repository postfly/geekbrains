number = int(input('Enter a positive integer: '))
num_max = 0
while number > 0:
    a = number % 10
    number = number // 10
    if a > num_max:
        num_max = a
print(num_max)

print('The work is done')
