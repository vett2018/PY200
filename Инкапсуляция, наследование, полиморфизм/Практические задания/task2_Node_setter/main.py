from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        # TODO заменить на вызов setter
        #self.next = None
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    # TODO заменить на getter и setter
    @property #next стал приватным
    def next(self):
        return self.__next #заменили на приватный атрибут, нужно создать setter так как подчеркивает приватный атрибут __next
    #getter что то возращает
    #setter устанавливает значение внутри

    @next.setter #выполняет присвоения
    def next(self, value):
        print('Вызван setter')
        self.is_valid(value) #корректность ввода
        self.__next = value

if __name__ == "__main__":
    first_node = Node(1)  # отработал setter в init
    second_node = Node(2)  # отработал setter в init

    first_node.next = second_node # не подконтрольно пользователю он не может своими руками залесть

    print(repr(first_node), repr(first_node.next))
