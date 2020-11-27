class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def dimensions(self):
        return len(self.my_list), len(self.my_list[0])

    def __add__(self, other):
        rows, cols = self.dimensions()
        new_list = self.my_list.copy()
        for i in range(rows):
            for j in range(cols):
                new_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix(new_list).__str__()


m = Matrix([[4, 2, 0, 7, 5], [2, 3, 5, 1, 9]])
new_m = Matrix([[1, 2, 8, 3, 4], [4, 3, 0, 0, 7]])

print(m.__add__(new_m))
