class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def get(self, index):
        list_length = self.find_linked_list_length()
        if index < 0 or index >= list_length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_linked_list_length(self):
        slow = self.head
        fast = self.head
        steps_by_slow = 0
        while fast and fast.next and fast.next.next:
            slow = slow.next
            steps_by_slow += 1
            fast = fast.next.next
        if fast.next:
            # list parity = 'even'
            list_length = (steps_by_slow + 1) * 2
        else:
            # list parity = 'odd'
            list_length = ((steps_by_slow + 1) * 2) - 1
        return list_length


def find_kth_from_end(linked_list: LinkedList, k: int):
    list_length = linked_list.find_linked_list_length()
    if k <= 0 or k > list_length:
        return None
    index = list_length - k
    return linked_list.get(index)

# Most optimal way to do so:
# def find_kth_from_end(ll, k):
#     slow = fast = ll.head
#     for _ in range(k):
#         if fast is None:
#             return None
#         fast = fast.next
#
#     while fast:
#         slow = slow.next
#         fast = fast.next
#
#     return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(5)
my_linked_list.append(3)
my_linked_list.append(5)


k = 8
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
