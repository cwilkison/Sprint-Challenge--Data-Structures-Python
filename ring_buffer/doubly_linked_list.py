"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    def __len__(self):
        return self.length
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # else set the new node's next pointer to the head
        # and set the new node's prev pointer to itself
        else:
            # moves the head to the next position, to create a space for the new node
            new_node.next = self.head
            # makes the former head's prev pointer point to the new node/head
            new_node.prev = new_node
            # makes the new node the new head
            self.head = new_node
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head:
            return None
        # reassign the next and prev pointers, which is being done by the delete()
        val = self.head.value
        self.delete(self.head)
        return val
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # move tail to second to last position by changing the former tail's prev pointer
            new_node.prev = self.tail
            # make new node/tail's next pointer point to itself
            self.tail.next = new_node
            # assign the new tail to new node
            self.tail = new_node
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(value)
        return value
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return None
        value = node.value
        self.delete(node)
        self.add_to_head(value)
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return None
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if the node is the head, change it's next pointer, delete it
        elif node is self.head:
            self.head = node.next
            node.delete()
        # if the node is the tail, change it's prev pointer, delete it
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    """Returns the highest value currently in the list"""
    def get_max(self):
        # store the current value
        value = self.head.value
        # store the current head
        current = self.head
        # while there is a head
        while current is not None:
            # if the current value is greater than the initial stored value
            if current.value > value:
                # set the initial value to the current value
                value = current.value
            # set the current head to the next pointer
            current = current.next
        return value