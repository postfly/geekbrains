class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Рисуем маркером')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()
