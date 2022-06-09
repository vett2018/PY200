from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.head: Optional[Node] = None  # TODO добавить указатель на первый элемент


        self.list_nodes = []
        if data is not None:
            self.init_linked_list(data)

    def init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [Node(value) for value in data]
        self.head = self.list_nodes[0]  # TODO инициализировать указатель на первый элемент

        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]
            next_node = self.list_nodes[i + 1]
            self.linked_nodes(current_node, next_node)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __repr__(self) -> str:
        return str(self.list_nodes)

    def step_by_step_on_nodes(self, index: int) -> Node: #пинает от ноды которая приходит к следующей ноде
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        # TODO проверка правильности типа индекса
        if not isinstance(index, int):
            raise TypeError

        current_node = self.head  # TODO чему равен начальный элемент?
        for _ in range(index):  # TODO с помощью цикла for добраться до нужного узла
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any: #регулируем встроенные функции #значение узлов
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)  # TODO метод должен возвращать значение узла
        return node.value


if __name__ == "__main__":
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    print(linked_list[1])
