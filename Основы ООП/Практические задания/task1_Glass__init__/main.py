from typing import Union


class Glass: #класс
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]): #атрибуты класса union оператор обьеденения типа данных int или float
        #  TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)): #проверка на тип данных
            raise TypeError
        if not capacity_volume > 0: #
            raise ValueError
        self.capacity_volume = capacity_volume #объем стакана атрибуты нашего класса
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0: # проверка на занятый объем
            raise ValueError
        self.occupied_volume = occupied_volume #объем жидкости в стакане атрибуты нашего класса


if __name__ == "__main__":
    glass1 = Glass(200, 120) # TODO инициализировать два объекта типа Glass
    glass2 = Glass(500, 50)
    print(glass1)
     # TODO попробовать инициализировать не корректные объекты

    # <__main__.Glass object at 0x0000029A8E1ABFA0>  main название модуля Glass название класса, ячейка памяти 0x0000029A8E1ABFA0