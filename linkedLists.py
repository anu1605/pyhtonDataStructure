class Node:
    def __init__(self, value) -> None:
        self.__data = value
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    def insert(self, value):
        node = Node(value)
        if self.__head == None:
            self.__head = node
            self.__tail = node

        else:
            self.__tail.set_next(node)
            self.__tail = node
        self.__count += 1

    def get_head(self):
        return self.__head.get_data()

    def get_tail(self):
        return self.__tail.get_data()

    def print(self):
        pointer = self.__head
        while pointer != None:
            print(pointer.get_data())
            pointer = pointer.get_next()

    def total_nodes(self):
        return self.__count
