number = int(input('Enter the number of seconds: '))
hour = number // 3600
minute = number // 60 - hour * 60
second = number - (hour * 3600 + minute * 60)
time = f"{hour:02}:{minute:02}:{second:02}"
# 02 означает, что резервируем не менее 2-х разрядов
# и если в переменную ничего не попадает, то записываем два нуля
print(time)
