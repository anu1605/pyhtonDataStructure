class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
        self.__count += 1

    def insert(self, position, data):
        new_node = Node(data)
        pointer = self.__head
        current_node = pointer

        if not position >= 0 or not position <= self.__count:
            print("index out of range")
            return

        if position == 0:
            new_node.set_next(self.__head)
            self.__head = new_node
            self.__count += 1
            return

        elif position == self.__count:
            self.add(data)
            return

        for i in range(self.__count+1):
            prev_node = current_node
            current_node = pointer

            if i == position:
                prev_node.set_next(new_node)
                new_node.set_next(current_node)

            else:
                pointer = pointer.get_next()

        self.__count += 1

    def search(self, data):
        pointer = self.__head
        index = 0
        while pointer != None:
            if pointer.get_data() == data:
                return index
            else:
                index += 1

            pointer = pointer.get_next()

        return -1

    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg
