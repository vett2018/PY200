import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node_value = 5 # TODO с помощью метода assertIsNone проверить следующий узел
        node = Node(node_value)
        msg = "при инициализации значение следующего узла не 0"
        self.assertIsNone(node.next, msg)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        second_node = Node("second_node")  # TODO проверить что узлы связались
        first_node = Node("second_node", next_= second_node)
        expected_value = second_node
        actual_value = first_node.next

        msg = "узлы не эквивалентны"
        self.assertIs(expected_value, actual_value, msg)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node_value = 5  # TODO проверить метод __repr__ без следующего узла
        node = Node(node_value)
        expected_value = f"Node({node_value}, None)"
        actual_value = repr(node)
        msg = "Значение представления __repr__ некорректно для узла без следующего узла. "
        self.assertEqual(expected_value, actual_value, msg)

    ...  # TODO пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        expected_value = str(some_value)

        self.assertEqual(expected_value, str(node)) # TODO проверить строковое представление
        self.assertEqual(expected_value, f"{node}")

    def test_is_valid(self):
        Node.is_valid(Node(5))  # TODO проверить метод is_valid при корректных узлах
        Node.is_valid(None)

        with self.assertRaises(TypeError): # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
            invalid_node = "Invalid_node"
            Node.is_valid(invalid_node)
