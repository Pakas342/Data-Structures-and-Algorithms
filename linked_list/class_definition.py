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

    def pop(self):
        if not self.head:
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        pre.next = None
        self.tail = pre
        self.length -= 1
        return temp.value


example_linked_list = LinkedList(1)
example_linked_list.append(5)
example_linked_list.print()
example_linked_list.pop()
example_linked_list.print()