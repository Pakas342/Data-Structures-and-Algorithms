class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = temp.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        # if index >= self.length or index < 0:
        if index >= self.length or index < -self.length:
            return None
        if index >= 0:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
        else:
            if abs(index) <= self.length/2:
                temp = self.tail
                for _ in range(abs(index) - 1):
                    temp = temp.prev
            else:
                temp = self.head
                for _ in range(self.length + index):
                    temp = temp.next

        return temp
