class Poind2D:
    # инициализация
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # метод вывода
    def __str__(self):
        return f'Точка: ({self.x}, {self.y})'

    # def distance(self):
        # return (self.x ** 2 + self.y ** 2) ** 0.5
    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2) ** 0.5


p = Poind2D(2, 3)
# print(p.x, p.y)
print(p)
# print(p.distance())
# print(p, type(p))
print(p.point_distance(3,4))