class LLNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class Node(LLNode):

    def __init__(self, value):
        super().__init__(value)
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, value):
        node = LLNode(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop_first(self):
        if self.isempty():
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        return temp

    def append(self, value):
        node = LLNode(value)
        if self.isempty():
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.size += 1

    def pop(self):
        if self.isempty():
            return None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        node = temp.next
        temp.next = None
        self.size -= 1
        return node

    def isempty(self):
        return self.size == 0

    def len(self):
        return self.size


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, value):
        node = Node(value)
        if self.isempty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def pop_first(self):
        if self.isempty():
            return None
        temp = self.head
        if self.len() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.size -= 1
        return temp

    def append(self, value):
        node = Node(value)
        if self.isempty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.isempty():
            return None
        temp = self.tail
        if self.len() == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.size -= 1
        return temp

    def isempty(self):
        return self.size == 0

    def len(self):
        return self.size
