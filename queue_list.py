class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__top = max_size

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        return self.__top <= -1

    def is_empty(self):
        return self.__top == self.__max_size

    def push(self, data):

        self.__top -= 1

        if self.is_full():
            self.__top += 1
            print("Stack is Full")
            return

        self.__elements[self.__top] = data

        return

    def pop(self):
        if self.is_empty():
            print("Cannot Delete Item From Empty Queue.")
            return
        temp = self.__elements[self.__top]
        self.__elements[self.__top] = None
        self.__top += 1
        return temp

    def display(self):
        index = self.__top
        while index != self.__max_size:
            print(self.__elements[index])
            index += 1
