def user_data(**kwargs):
    return kwargs


name = input('Укажите имя: ')
surname = input('Укажите фамилию: ')
year_birth = int(input('Укажите год рождения: '))
city_residence = input('Укажите город проживания: ')
email = input('Укажите email: ')
phone = int(input('Укажите номер телефона: '))

result = user_data(Имя=name, Фамилия=surname, Год_рождения=year_birth, Город_проживания=city_residence, Email=email,
                   Телефон=phone)
print(result)
