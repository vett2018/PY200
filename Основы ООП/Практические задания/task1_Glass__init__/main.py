from typing import Union


class Glass: #класс
    def __init__(self, x: Union[int, float], y: Union[int, float]): #параметры класса union оператор обьеденения типа данных int или float
        #  TODO инициализировать объект "Стакан"
        if not isinstance(x, (int, float)): #проверка на тип данных
            raise TypeError
        if not x > 0: #
            raise ValueError
        self.capacity_volume = x #объем стакана атрибуты нашего класса
        if not isinstance(y, (int, float)):
            raise TypeError
        if y < 0: # проверка на занятый объем
            raise ValueError
        self.occupied_volume = y #объем жидкости в стакане атрибуты нашего класса


if __name__ == "__main__":
    glass1 = Glass(200, 120) # TODO инициализировать два объекта типа Glass
    glass2 = Glass(500, 50)
    print(glass1)
     # TODO попробовать инициализировать не корректные объекты

    # <__main__.Glass object at 0x0000029A8E1ABFA0>  main название модуля Glass название класса, ячейка памяти 0x0000029A8E1ABFA0