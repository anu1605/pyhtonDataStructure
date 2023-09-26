class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__top = -1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        return self.__top >= self.__max_size

    def is_empty(self):
        return self.__top == -1

    def push(self, data):

        self.__top += 1

        if self.is_full():
            print("Stack is Full")
            return

        self.__elements[self.__top] = data

        return

    def pop(self):
        if self.is_empty():
            print("Cannot Delete Item From Empty Stack.")

        temp = self.__elements[self.__top]
        self.__elements[self.__top] = None
        self.__top -= 1
        return temp

    def display(self):
        for element in self.__elements:
            if element == None:
                return
            print(element)
