class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__previous = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_previous(self):
        return self.__previous

    def get_next(self):
        return self.__next

    def set_previous(self, previous_node):
        self.__previous = previous_node

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
            new_node.set_previous(self.__tail)
            self.__tail = new_node
        self.__count += 1

    def insert(self, position, data):
        new_node = Node(data)
        pointer = self.__head
        current_node = pointer

        if position < 0 or position > self.__count:
            print("index out of range")
            return

        if position == 0:
            new_node.set_next(self.__head)
            self.__head.set_previous(new_node)
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
                new_node.set_previous(prev_node)
                new_node.set_next(current_node)
                current_node.set_previous(new_node)

            else:
                pointer = pointer.get_next()

        self.__count += 1

    def search(self, data):
        pointer = self.__head
        while pointer != None:
            if pointer.get_data() == data:
                return pointer
            else:
                pointer = pointer.get_next()

        return None

    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

    def display_reverse(self):
        temp = self.__tail
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_previous()

    def delete(self, data):
        current_node = self.__head
        prev_node = current_node

        while current_node != None:
            if current_node.get_data() == data:
                if current_node == self.__head:
                    self.__head = self.__head.get_next()
                    return
                if current_node == self.__tail:
                    self.__tail = prev_node
                    self.__tail.set_next(None)
                    return
                prev_node.set_next(current_node.get_next())
                current_node.set_next(None)
                return
            else:
                prev_node = current_node
                current_node = current_node.get_next()

    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg
