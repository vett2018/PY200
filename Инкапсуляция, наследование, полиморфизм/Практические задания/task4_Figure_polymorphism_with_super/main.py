class Rectangle: # вычисление площади не в кв метрах, а в футах квадратных
    """ Базовый класс. """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class RectangleFoot(Rectangle):
    """ Производный класс. Прямоугольник в футах """
    FOOT_IN_METERS = 0.3048  # столько метров в один футе

    def area(self):
        """ Переводим площадь в футы. """
        area = super().area()  # TODO вызываем метод area базового класса  # вызываем метод который зашит в базовом класс
        return area / (self.FOOT_IN_METERS ** 2)


if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(rect.area())

    rect_foot = RectangleFoot(5, 10)
    print(rect_foot.area())
