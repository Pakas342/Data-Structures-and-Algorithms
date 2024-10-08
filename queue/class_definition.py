class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        current_node = self.first
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first, self.last = new_node, new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            node_to_return = self.first
            self.first, self.last = None, None
        else:
            node_to_return = self.first
            self.first = node_to_return.next
            node_to_return.next = None
        self.length -= 1
        return node_to_return
