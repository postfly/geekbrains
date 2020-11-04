a = int(input('number of kilometers on the first day: '))
b = int(input('desired result in kilometers: '))
day = 1
while a <= b:
    a *= 1.1
    day += 1
    print(a)
print('On', day, 'day the result will be achieved')
print('The work is done')
