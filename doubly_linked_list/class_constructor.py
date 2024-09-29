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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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

    def set_value(self, index, value):
        node_to_change = self.get(index)
        if not node_to_change:
            return False
        node_to_change.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif 0 < index < self.length:
            before = self.get(index - 1)
            new_node = Node(value)
            after = before.next

            new_node.next = after
            after.prev = new_node
            before.next = new_node
            new_node.prev = before

            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == (self.length - 1):
            return self.pop()
        elif 0 < index < self.length:
            before = self.get(index - 1)
            temp = before.next
            after = before.next.next

            temp.next = None
            temp.prev = None

            after.prev = before
            before.next = after

            self.length -= 1
            return temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()
