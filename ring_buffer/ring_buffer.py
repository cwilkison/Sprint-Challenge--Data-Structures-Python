from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            #current node becomes head
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            #if current node does not have a next
            #make current node headf
            if not self.current.next:
                self.current.value = item
                self.current = self.storage.head
            else:
            #current node moves over to replace next
                self.current.value = item
                self.current = self.current.next


    def get(self):
        buffer = []
        node = self.storage.head
        while node:
            buffer.append(node.value)
            node = node.next
        return buffer