n = input('Enter a positive integer: ')
while n:
    if n.isdigit():
        # функция .isdigit() проверяет, состоит ли строка
        # только из цифр
        result = f"{int(n) + int(n * 2) + int(n * 3)}"
        print(result)
        break
    else:
        print("Number must be whole and positive")
        n = input('Enter a positive integer: ')
