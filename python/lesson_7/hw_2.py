from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @staticmethod
    def sum_cons(x, y):
        return x + y

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return 2 * self.param + 0.3


coat = Coat(500)
costume = Costume(120)

print(coat.consumption)
print(costume.consumption)
print(Clothes.sum_cons(coat.consumption, costume.consumption))
