import math

#полиморфизм при наследовании
class Figure: #азовый класс
    """ Базовый класс. """

    def area(self): #метод
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure): # super не нужно вызывать потому что нет конструктора в базовом классе
    """ Производный класс. Прямоугольник. """

    def __init__(self, a, b):  # TODO определить конструктор и перегрузить метод area
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return self.a * self.b


class Circle(Figure):
    """ Производный класс. Круг. """

    def __init__(self, r):   # TODO определить конструктор и перегрузить метод area
       self.r = r

    def area(self):
        super().area()
        return 3.14 * self.r ** 2


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
