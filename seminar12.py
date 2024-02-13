# Стек должен поддерживать следующие операции:
# S.push(e): добавление элемента e на вершину стека S.
# S.pop(): удаляет и возвращает верхний элемент стека S. Если стек пуст, то возникает ошибка.
# S.top(): возвращает верхний элемент стека S, не удаляя его. Если стек пуст, то возникает ошибка.
# S.is_empty( ): возвращает True если стек S не содержит ни одного элемента.
# len(S): возвращает текущеее количество элементов в стеке S.

# #2
# class Stroke_processing():
#
#     '''анализ строки заданными функциями'''
#
#     def __init__(self, possible_lenght):
#         self.stack = []
#         self.possible_lenght = possible_lenght
#
#     def push(self, element):
#         if len(self.stack) >= self.possible_lenght:
#             return Exception('allowed number of elements has been exceeded')
#         self.stack.append(element)
#
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return Exception('Element cant be removed from empty list')
#         popped = self.stack.pop()
#         return popped
#
#
#     def top(self):
#         if len(self.stack) == 0:
#             return Exception('Element cant be returned from empty list')
#         return self.stack[-1]
#
#
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         return False
#
#     def __len__(self):
#         return len(self.stack)
#
#
#     def show(self):
#         return self.stack
#
# example1 = '((dsasdas((das(d)das)d)asd)da)'
# example2 = '(f(gfhd((hgfdg((fghh)dads)das))ds)adddads())))'
# example3 = input()
# examples = (example1, example2, example3)
#
# def example_analyse(sequence):
#
#     stack = Stroke_processing(40)
#
#     for element in sequence:
#         if element in '({[':
#             stack.push(element)
#             print(len(stack), stack.show())
#         if (element == ')' and stack.top() == '(') or (element == '}' and stack.top() == '{') or (element == ']' and stack.top() == '['):
#             if stack.is_empty():
#                 return 'incorrect parentheses'
#             stack.pop()
#     if stack.is_empty():
#         return 'correct parentheses'
#     return 'incorrect parentheses'
#
#
# for stroke in examples:
#     print(example_analyse(stroke))

# # 3
# Реализовать класс однонаправленного связанного списка.
#
# class LinkedList():
#     head = None
#
#     class Node():
#         element = None
#         next_node = None
#
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#
#     def add(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             return element
#
#         node = self.head
#
#         while node.next_node:
#             node = node.next_node
#
#         node.next_node = self.Node(element)
#
#     def show(self):
#         node = self.head
#
#         while node.next_node:
#             print(node.element)
#             node = node.next_node
#
#
# linked_list = LinkedList()
#
# linked_list.add(14)
# linked_list.add(3)
# linked_list.add(12354)
# linked_list.add(88)
# linked_list.add(76)
#
# print(linked_list.show())
