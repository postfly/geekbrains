class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        add_cell = self.number + other.number
        return add_cell

    def __sub__(self, other):
        sub_cell = self.number - other.number
        if sub_cell == 0:
            print('Похоже мы уничтожили клетки')
        else:
            return sub_cell

    def __mul__(self, other):
        mul_cell = self.number * other.number
        return mul_cell

    def __truediv__(self, other):
        truediv_cell = self.number // other.number
        return truediv_cell

    def make_order(self, col):
        result = ''
        for i in range(self.number // col):
            result += '*' * col + '\n'
        result += '*' * (self.number % col) + '\n'
        return result


cell = Cell(11)

new_cell = Cell(11)
print(cell.__add__(new_cell))
print(cell.__sub__(new_cell))
print(cell.__mul__(new_cell))
print(cell.__truediv__(new_cell))
print(cell.make_order(4))
