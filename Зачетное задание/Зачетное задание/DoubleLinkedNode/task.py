class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any):
        """
        Инициализация атрибутов класса
        :param value:
        """
        self.value = value
        self.next = None

    def __str__(self):


    def __repr__(self):
        ...


class DoubleLinkedNode(Node):
    ...


if __name__ == "__main__":
    ...
