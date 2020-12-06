class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


c_1 = ComplexNumber(4, -8)
c_2 = ComplexNumber(6, 11)

print(c_1 + c_2)
print(c_1 * c_2)
