# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:
from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list
        (right after the front sentinel)
        """
        # Create a new node using the provided value
        node = SLNode(value)

        # Set the next attribute of the new node to the current first node
        # in the list
        node.next = self._head.next

        # Set next attribute of the front sentinel to new node
        self._head.next = node


    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list
        """

        # Create a new node using the provided value
        new_node = SLNode(value)

        # Sets node to the head of the list
        node = self._head

        # Traverses the list until it finds the last node
        while node.next:
            node = node.next

        # Once the end is reached, sets the next attribute of the
        # last node to the new_node
        node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        his method inserts a new value at the specified index position in the linked list
        """

        # Checks if index is invalid, raises an Exception
        if index < 0 or index > self.length():
            raise SLLException

        # Sets new_node to value
        # Sets node to the head to be able to iterate the SLL
        new_node = SLNode(value)
        node = self._head

        # Sets node to the next node index number of times
        for i in range(index):
            node = node.next

        # Once desired index is reached, sets the next attributes of the nodes
        new_node.next = node.next
        node.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified
        index position from the linked list.
        """

        # Checks for valid index
        if index < 0 or index >= self.length():
            raise SLLException

        # Sets the node to head of the SLL
        node = self._head

        # Iterates through the list until it
        # finds the node before the removal
        for i in range(index):
            node = node.next

        # Sets the nodes next attribute to the node after the one being removed
        node.next = node.next.next




    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end,
        and removes the first node that matches the provided “value” object
        """
        # Sets node to head of the list
        node = self._head

        # Iterates through the SLL
        while node.next:

            # Checks if nodes value is equal to the given value
            if node.next.value == value:

                # if yes, resets the currents nodes next attribute
                # to the matching nodes next
                node.next = node.next.next
                return True

            node = node.next

        # If value wasn't found
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list
        that match the provided “value” object
        """

        # Initializes count and sets node to head for iteration
        count = 0
        node = self._head

        # Iterates through until value equals value of node
        while node.next:

            # If found, add 1 to count
            if node.next.value == value:
                count += 1

            node = node.next

        return count

    def find(self, value: object) -> bool:
        """
        This method returns a Boolean value based on whether or not the provided “value” object
        exists in the list
        """

        node = self._head

        # Returns True if value is found
        while node.next:
            if node.next.value == value:
                return True

            node = node.next

        # False if not
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList object that contains the
        requested number of nodes from the original list, starting with the
        node located at the requested start index.
        """

        # Checks for valid bounds for slicing
        if start_index < 0 or start_index >= self.length():
            raise SLLException
        if size < 0 or start_index + size > self.length():
            raise SLLException

        # Node is set as the first node in the list
        node = self._head.next

        # LinkedList obj created to store the desired slice
        slice_list = LinkedList()

        # Iterated to find desired index to begin slice
        for i in range(start_index):
            node = node.next

        # Iterates over the next nodes, inserts each of those values
        # into the newly created LinkedList obj
        for i in range(size):
            slice_list.insert_back(node.value)
            node = node.next

        return slice_list



if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
