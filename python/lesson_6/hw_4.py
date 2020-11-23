class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'The {self.name} is color {self.color} went')

    def stop(self):
        if self.speed == 0:
            print(f'The {self.name} has stopped')

    def turn(self, direction):
        if self.speed > 0:
            print(f'The {self.name} turned on the {direction}')

    def show_speed(self):
        print(f'Speed {self.name} is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Over speed')
        else:
            print(f'Speed {self.name} is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f'Over speed')
        else:
            print(f'Speed {self.name} is {self.speed}')


class PoliceCar(Car):
    pass


town = TownCar('BMW', 'dark', 60)
town.go()
town.show_speed()
town.turn('left')
town.stop()
print()
sport = SportCar('Ferrari', 'red', 120)
sport.go()
sport.show_speed()
sport.turn('straight')
sport.stop()
print()
work = WorkCar('Zil', 'blue', 45)
work.go()
work.show_speed()
work.turn('left')
work.stop()
print()
police = PoliceCar('Ford', 'silver', 0, True)
police.go()
police.show_speed()
police.turn('left')
police.stop()
