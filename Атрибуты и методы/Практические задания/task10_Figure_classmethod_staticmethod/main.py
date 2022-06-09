import math


class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """
    #метод экземпляра класса
    @classmethod
    def area(cls, *args): #падает любое кол-во аргументов
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            self.area_by_height(*args) #метод
        if len(args) == 3:
            self.area_by_angle(*args)

    @staticmethod
    def area_by_angle(a, b, angle):
        """ Формула площади по двум сторонам и углу между ними. """
        return 0.5 * a * b * math.sin(angle)

    @staticmethod
    def area_by_height(a, h):
        """ Формула площади по основанию и высоте. """
        return 0.5 * a * h


if __name__ == '__main__':
    #иницилизация экземпляров класса
    TriangleCalculator().area()  # Работаем через экземпляр
    TriangleCalculator().area_by_height(5, 10)  # Работаем через экземпляр
    #работаем с обьектом класса
    TriangleCalculator.area()  # Работаем через класс
    TriangleCalculator.area_by_height(5, 10)  # Работаем через класс

'экземпляр готовый продукт, сам класс как это делается'