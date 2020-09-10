class Poind2D:
    # инициализация
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # метод вывода
    def __str__(self):
        return f'Точка: ({self.x}, {self.y})'
    # Перегрузка "+"
    def __add__(self, other):
        return Poind2D(self.x + other.x + self.y + other.y)

    # def distance(self):
        # return (self.x ** 2 + self.y ** 2) ** 0.5
    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2) ** 0.5


p = Poind2D(2, 3)
q = Poind2D(3, 4)
# print(p.x, p.y)
print(p)
print(q)
# print(p.distance())
# print(p, type(p))
print(p.point_distance(3,4))