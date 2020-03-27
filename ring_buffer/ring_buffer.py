from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)
            if self.storage.__len__() == self.capacity:
                self.current = self.storage.head
        else:
            self.current.value = item
            if self.current.next != None:
                self.current = self.current.next
            else:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        cursor = self.storage.head
        while cursor != None:
            list_buffer_contents.append(cursor.value)
            cursor = cursor.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
