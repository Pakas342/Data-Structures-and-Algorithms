class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None
        self.tail = prev
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            prev = self.get(index - 1)
            new_node = Node(value)
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == (self.length - 1):
            return self.pop()
        prev = self.get(index - 1)
        # I do this instead of temp = self.get(index) because prev.next is O(1) and self.get is O(n)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


example_linked_list = LinkedList(1)
example_linked_list.append(5)
example_linked_list.print()
example_linked_list.pop()
example_linked_list.print()
