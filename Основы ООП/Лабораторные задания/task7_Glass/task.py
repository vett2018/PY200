from typing import Union


class Glass: # TODO  создать класс Glass
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not  occupied_volume > 0:
            raise ValueError
        self.occupied_volume = occupied_volume




if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)



""" 
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO заменить на метод
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане



#  TODO создать метод, который будет инициализировать атрибут capacity_volume
    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана


if __name__ == "__main__":
    g = Glass(200, 100)  # TODO инициализировать экземпляр класса Glass
    print(g.capacity_volume)  # TODO распечатать атрибут capacity_volume
    print(g.occupied_volume)  # TODO распечатать атрибут occupied_volume
"""

