from typing import Iterable
from abc import ABC, abstractmethod


# с помощью драйвера выведим файл в формат txt, написать драйвер который будет принимать из связного списка
# данные и сохранять их в тхт файл

class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename: str):  # TODO реализовать драйвер работы с текстовым файлом
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as file:
            return [int(value.rstrip()) for value in file]
        pass

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as file:
            for value in data:
                file.write(str(value) + "\n")
        pass

    # TODO реализовать метод чтения данных из файла

    # TODO реализовать метод записи в файл построчно

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('output.txt')
    driver.write(write_data) #запись файла построчно

    read_data = driver.read()
    print(read_data)
