class Date:
    def __init__(self, date):
        self.date = date.split('-')

    @classmethod
    def number(cls, date):
        day, month, year = date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def num_valid(date):
        day, month, year = date.split('-')
        if int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12 or int(year) > 0:
            return f'Вы указали неверный формат даты'
        return f'Формат даты указан верно'


print(Date.number('12-12-2020'))
print(Date.num_valid('12-13-2020'))
