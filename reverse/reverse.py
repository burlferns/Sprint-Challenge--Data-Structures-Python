class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_listOFF(self, node, prev):
        # You must use recursion for this solution
        pass

    # Renamed the parameter names to be more meaningful
    # oldL refers to the old list that needs reversing
    # newL refers to the new list that is the reverse of the oldL
    def reverse_list(self, oldL, newL):
        # You must use recursion for this solution

        # Base cases
        if oldL == None:
            self.head = newL
            return
        
        # Recursive cases
        if newL == None:
            newL = oldL
            oldL = oldL.get_next()
            newL.set_next(None)
            self.reverse_list(oldL,newL)
            return
        else:
            oldL_head = oldL
            oldL = oldL.get_next()
            oldL_head.set_next(newL)
            newL = oldL_head
            self.reverse_list(oldL,newL)
            return


# def printLL(head):
#     curr_node = head
#     while curr_node != None:
#         print(curr_node.get_value(), end="", flush=True)
#         if curr_node.get_next() != None:
#             print("->", end="", flush=True)
#         curr_node = curr_node.get_next()
#     print("")

# listA = LinkedList()
# listA.add_to_head(5)
# listA.add_to_head(4)
# listA.add_to_head(3)
# listA.add_to_head(2)
# listA.add_to_head(1)

# print("The original list:")
# printLL(listA.head)

# listA.reverse_list(listA.head,None)

# print("The reversed list:")
# printLL(listA.head)    