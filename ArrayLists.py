import numpy as np


class ArrayList:

    count = 0

    def createArray(self, size):
        self.array = np.zeros(size, dtype=int)

    def __init__(self) -> None:
        self.size = 10
        self.createArray(self.size)

    def insert(self, value):
        if self.count >= len(self.array):
            self.newArray(self.array)
            self.array[self.count] = value
            self.count += 1

        else:
            self.array[self.count] = value
            self.count += 1

    def printArray(self):
        if self.count == 0:
            print("Array is Empty")
        for i in range(self.count):
            print(self.array[i], " ", end="")

    def newArray(self, array):
        prevArray = array
        newsize = len(self.array) * 2
        self.array = np.zeros(newsize, dtype=int)
        for i in range(self.count):
            self.array[i] = prevArray[i]

    def addElementAt(self, value, index):
        if index >= len(self.array):
            self.newArray(self.array)

        currentArray = self.getArray()

        # in the begining
        if index == 0:
            self.array[0] = value
            for i in range(self.count):
                self.array[i+1] = currentArray[i]
            self.count += 1

        # at the end
        elif index >= self.count:
            self.array[self.count] = value
            self.count += 1

        # in between
        elif index > 0 and index < self.count:
            self.array[index] = value
            for i in range(index, self.count):
                self.array[i+1] = currentArray[i]
            self.count += 1

    def delete(self, index):
        if self.count == 0:
            print("Cannot Perform Delete Operation. Array is Empty")

        elif index >= self.count:
            print("Index out of Bound")

        else:
            currentArray = self.getArray()
            # in the begining
            if index == 0:
                for i in range(self.count):
                    self.array[i] = currentArray[i+1]
                self.count -= 1

            # at the end
            elif index == self.count:
                self.array[index] = 0
                self.count -= 1

            # in between
            elif index > 0 and index < self.count:
                for i in range(index, self.count):
                    self.array[i] = currentArray[i+1]
                self.count -= 1

    def getArray(self):
        currentArray = np.zeros(len(self.array))
        for i in range(self.count):
            currentArray[i] = self.array[i]
        return currentArray
