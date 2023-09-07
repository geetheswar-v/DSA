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
