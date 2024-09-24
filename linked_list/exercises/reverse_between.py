class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    # My first implementation, works, but is too much code
    # def reverse_between(self, start_index: int, end_index: int):
    #     if start_index < 0 or end_index >= self.length or start_index > end_index:
    #         return None
    #     temp = self.head
    #     prev = None
    #     for _ in range(start_index):
    #         prev = temp
    #         temp = prev.next
    #     temp_head = temp
    #     prev_temp_head = prev
    #     for _ in range(start_index, end_index + 1, 1):
    #         after = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = after
    #     temp_tail = prev
    #     after_tail = temp
    #     temp_head.next = None
    #
    #     if prev_temp_head:
    #         prev_temp_head.next = temp_tail
    #     if after_tail:
    #         temp_head.next = after_tail
    #     if temp_head == self.head:
    #         self.head = temp_tail


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 3)
print("Reversed sublist (2, 3): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None

"""