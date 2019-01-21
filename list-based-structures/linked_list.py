"""
Implementation of linked lists in python

Linked list will have a head element that is the first element in the list.
Append - add a new element at the end of the linked list.
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # if item has a head, iterate till the end of list
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is 1.
        Return None if position is not in the list.
        """
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and position >= counter:
            if position == counter:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """
        Insert a new node at the given position.
        Assume the first position is 1.
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        """
        current = self.head
        counter = 1
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = current.next
            current = new_element

    def delete(self, value):
        # delete first element with the value
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                current = current.next
        return None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value