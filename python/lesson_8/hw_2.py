class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    user_num_1 = int(input('Введите делимое: '))
    user_num_2 = int(input('Введите делитель: '))
    if user_num_2 == 0:
        raise MyError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except MyError as err:
    print(err)
else:
    res = user_num_1 / user_num_2
    print(res)
