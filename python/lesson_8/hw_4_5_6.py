class Warehouse:
    def __init__(self):
        pass


class OfficeEquipment:
    def __init__(self, name, cost, quantity, department):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.department = department
        self.items = {}
        # self.items = {'Модель устройства': self.name, 'Цена за ед': self.cost, 'Количество': self.quantity,
        #               'Департамент': self.department}

    @staticmethod
    def acceptance():
        try:
            items = {}
            name = input('Введите название: ')
            cost = int(input('Введите стоимость: '))
            quantity = int(input('Введите количество: '))
            department = input('Укажите департамерт: ')
            item = {'Модель устройства': name, 'Стоимость': cost, 'Количество': quantity, 'Департамент': department}
            items.update(item)
            print(items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, cost, department, print_speed):
        super().__init__(name, quantity, cost, department)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, cost, department, scanning_speed):
        super().__init__(name, quantity, cost, department)
        self.scanning_speed = scanning_speed


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, cost, department, copy_speed):
        super().__init__(name, quantity, cost, department)
        self.copy_speed = copy_speed


OfficeEquipment.acceptance()
