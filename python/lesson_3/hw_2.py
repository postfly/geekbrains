def user_data(name, surname, year_birth, city, email, phone):
    return f'Name: {name}\n' \
           f'Surname: {surname}\n' \
           f'Year birth: {year_birth}\n' \
           f'City: {city}\n' \
           f'Email: {email}\n' \
           f'Phone: {phone}\n'

print(user_data(name='Vadim',
                surname='Besputin',
                year_birth='11.06.1981',
                city='Moscow',
                email='postfly@mail.ru',
                phone='+79000000000'))
