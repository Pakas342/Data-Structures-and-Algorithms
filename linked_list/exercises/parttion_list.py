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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    # This solution is O(n) time complex, and O(n) space complex, which isn't the best, but does the job
    # def partition_list(self, x):
    #     if not self.head:
    #         return False
    #     left = []
    #     right = []
    #     temp = self.head
    #     while temp:
    #         if temp.value < x:
    #             left.append(temp.value)
    #         else:
    #             right.append(temp.value)
    #         temp = temp.next
    #     full_list = left + right
    #     prev_node = None
    #     for value in full_list:
    #         new_node = Node(value)
    #         if not prev_node:
    #             self.head = new_node
    #         else:
    #             prev_node.next = new_node
    #         prev_node = new_node
    #         continue
    #     return True

    # Second solution, with O(n) time complex and O(1) space complex
    # def partition_list(self, x):
    #     if not self.head:
    #         return False
    #     left_last_node = None
    #     left_head = None
    #     right_last_node = None
    #     right_head = None
    #     temp = self.head
    #     while temp:
    #         if temp.value < x:
    #             if not left_last_node:
    #                 left_head = temp
    #             else:
    #                 left_last_node.next = temp
    #             left_last_node = temp
    #         else:
    #             if not right_last_node:
    #                 right_head = temp
    #             else:
    #                 right_last_node.next = temp
    #             right_last_node = temp
    #         temp = temp.next
    #     if left_head:
    #         self.head = left_head
    #     elif right_head:
    #         self.head = right_head
    #     if left_head and right_head:
    #         left_last_node.next = right_head
    #         right_last_node.next = None
    #     elif left_head:
    #         left_last_node.next = None
    #     return True

    # Third solution, more elegant without requiring all the if statements
    def partition_list(self, x):
        if not self.head:
            return False

        left_dummy = Node(0)  # Dummy node for left partition
        right_dummy = Node(0)  # Dummy node for right partition
        left = left_dummy
        right = right_dummy

        current = self.head
        while current:
            if current.value < x:
                left.next = current
                left = current
            else:
                right.next = current
                right = current
            current = current.next

        left.next = right_dummy.next
        right.next = None
        self.head = left_dummy.next

        return True


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        print(f'Node : {current.value}')
        current = current.next
    return result


# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
