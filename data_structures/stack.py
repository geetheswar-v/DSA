from data_structures import LinkedList


class Stack:

    def __init__(self):
        self.__stack = LinkedList()

    def push(self, value):
        self.__stack.prepend(value)

    def pop(self):
        return self.__stack.pop_first()

    def top(self):
        return self.__stack.head

    def len(self):
        return self.__stack.len()

    def isempty(self):
        return self.__stack.isempty()


class ListStack:

    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        if self.isempty():
            return None
        return self.pop()

    def top(self):
        if self.isempty():
            return None
        return self.__stack[-1]

    def isempty(self):
        return len(self.__stack) == 0

    def len(self):
        return len(self.__stack)
