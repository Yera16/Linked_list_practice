class Node:
## NODE CONSTRUCTOR HERE ##
   def __init__(self, value):
       self.value =  value
       self.next = None
#################################


class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
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

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 1:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
           return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

            # for i in range(self.length):
            #     if i == index:
            #         return temp.value
            #     temp = temp.next
            #     i += 1

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre = self.get(index-1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index-1)
        cur = pre.next
        pre.next = cur.next
        cur.next = None
        self.length -= 1
        return cur

    def reverse(self):
        if self.length == 0:
            return True
        if self.length == 1:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            return True
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        temp = self.head
        if self.head is None:
            return None
        while temp is not None:
            next_temp = temp.next  # Save next node
            temp.next = None  # Detach current node to avoid cycle

            if temp.value < x:
                prev1.next = temp
                prev1 = prev1.next  # Move prev1 to the last node in the lesser list
            else:
                prev2.next = temp
                prev2 = prev2.next  # Move prev2 to the last node in the greater or equal list

            temp = next_temp  # Move to the next node

        prev1.next = dummy2.next  # Connect lesser list with greater or equal list
        self.head = dummy1.next  # Update head

    def remove_duplicates(self):
            if not self.head or not self.head.next:
                return
            myset = set()
            temp = self.head
            myset.add(self.head.value)
            while temp.next is not None:
                if temp.next.value in myset:
                    temp.next = temp.next.next
                else:
                    myset.add(temp.next.value)
                    temp = temp.next
        # if not self.head or not self.head.next:
        #     return
        # myset = set()
        # temp = self.head
        # prev = self.head
        # while temp is not None:
        #     tl = len(myset)
        #     myset.add(temp.value)
        #     if len(myset) == tl:
        #         prev.next = temp.next
        #     prev = temp
        #     temp = temp.next


    def reverse_between(self, start_index, end_index):
        if start_index < 0 or start_index >= self.length or end_index < 0 or end_index >= self.length:
            return None
        if not self.head or not self.head.next:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(start_index):
            prev = prev.next

        curr = prev.next
        temp = None

        for i in range(start_index-end_index):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        if start_index == 0:
            self.head = dummy.next




#Exercise 1
def find_middle_node(self):
        fast = self.head
        slow = self.head
        if self.head is None:
            return slow
        if self.head == self.tail:
            return slow
        while fast is not None:
            if fast.next is  None:
                return slow
            fast = fast.next.next
            slow = slow.next
        return slow
#Exercise 2
def has_loop(self):
        fast = self.head
        slow = self.head
        if self.head is None:
            return False
        if self.head == self.tail:
            return False
        while fast is not None:
            if fast is slow or fast.next is slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False


# Exercise 3
def find_kth_from_end(linked_list, index):
    fast = linked_list.head
    slow = linked_list.head
    if linked_list.head is None:
        return None
    if linked_list.head == linked_list.tail:
        return None
    for i in range( index):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


# Function to convert linked list to Python list
# def linkedlist_to_list(head):
#     result = []
#     current = head
#     while current:
#         result.append(current.value)
#         current = current.next
#     return result
#
#
# # Function to test partition_list
# def test_partition_list():
#     test_cases_passed = 0
#
#     print("-----------------------")
#
#     # Test 1: Normal Case
#     print("Test 1: Normal Case")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     ll.append(1)
#     ll.append(4)
#     ll.append(2)
#     ll.append(5)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 2: All Equal Values
#     print("Test 2: All Equal Values")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     ll.append(3)
#     ll.append(3)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [3, 3, 3]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 3: Single Element
#     print("Test 3: Single Element")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(1)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 4: Already Sorted
#     print("Test 4: Already Sorted")
#     x = 2
#     print(f"x = {x}")
#     ll = LinkedList(1)
#     ll.append(2)
#     ll.append(3)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 2, 3]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 5: Reverse Sorted
#     print("Test 5: Reverse Sorted")
#     x = 2
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     ll.append(2)
#     ll.append(1)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 3, 2]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 6: All Smaller Values
#     print("Test 6: All Smaller Values")
#     x = 2
#     print(f"x = {x}")
#     ll = LinkedList(1)
#     ll.append(1)
#     ll.append(1)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [1, 1, 1]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Test 7: Single Element, Equal to Partition
#     print("Test 7: Single Element, Equal to Partition")
#     x = 3
#     print(f"x = {x}")
#     ll = LinkedList(3)
#     print("Before:", linkedlist_to_list(ll.head))
#     ll.partition_list(x)
#     print("After:", linkedlist_to_list(ll.head))
#     if linkedlist_to_list(ll.head) == [3]:
#         print("PASS")
#         test_cases_passed += 1
#     else:
#         print("FAIL")
#
#     print("-----------------------")
#
#     # Summary
#     print(f"{test_cases_passed} out of 7 tests passed.")
#
#
# # Run the test function
# test_partition_list()
#
# #
# index = 1
#
# my_linked_list = LinkedList(6)
# my_linked_list.append(5)
# my_linked_list.append(4)
# my_linked_list.append(3)
# my_linked_list.append(2)
# my_linked_list.append(1)
#my_linked_list.append(0)
#my_linked_list.pop()
#my_linked_list.pop()
#my_linked_list.pop()
# my_linked_list.prepend(5)
#my_linked_list.pop_first()
# my_linked_list.get(3)
#my_linked_list.set_value(2, 0)
#my_linked_list.insert(index, 0)



# print('Head:', my_linked_list.head.value)
# print('Next:', my_linked_list.head.next)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# print(my_linked_list.insert(index, 0))
# my_linked_list.print_list()
# # print(f'The value at {index} is: ', my_linked_list.get(index))
# # my_linked_list.remove(0)
# my_linked_list.reverse()
# print("\n")
# x = my_linked_list.find_middle_node()
# # print(x)
# x = find_kth_from_end(my_linked_list, index).value
# print(x)
# my_linked_list.print_list()
# print("\n")

#print('Length:', my_linked_list.length)
