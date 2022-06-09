from typing import Iterable, Optional

from node import Node
#помещаем узлы,

class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.list_nodes = [] #пустой список, куда будем класть узлы
        if data is not None: #проверка даты(лист)
            self.init_linked_list(data)

    def init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [Node(value) for value in data] # TODO обернуть все значения в класс Node и поместить их в python список
        #value индекс забирает из даты
        for i in range(len(self.list_nodes) - 1): #цикл организовывет связку   # TODO составьте алгоритм, который свяжет узлы
            self.linked_nodes(self.list_nodes[i], self.list_nodes[i+1]) #отправляем два аргумента, метод соеденяет элемент левый и правый
    @staticmethod    # TODO каким должен быть этот метод?
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None: #иницилизируем весь список
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __str__(self) -> str:
        return str(self.list_nodes)


if __name__ == "__main__":
    list_ = [1, 2, 3] #содержит data
    linked_list = LinkedList(list_) #итерируемый объект
    print(linked_list)
