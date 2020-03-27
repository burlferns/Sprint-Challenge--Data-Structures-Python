class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self

        while (value >= current_node.value and current_node.right != None) or \
            (value < current_node.value and current_node.left != None):
            if value >= current_node.value: # Handles > & =
                current_node = current_node.right
            else:
                current_node = current_node.left
        
        if value >= current_node.value: # Handles > & =
            current_node.right = BinarySearchTree(value)
            return
        if value < current_node.value:
            current_node.left = BinarySearchTree(value)
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self

        while (target > current_node.value and current_node.right != None) or \
            (target < current_node.value and current_node.left != None):
            if target > current_node.value: 
                current_node = current_node.right
            else:
                current_node = current_node.left

        if target == current_node.value:
            return True
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self

        while current_node.right != None:
            current_node = current_node.right
            
        return current_node.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            cb(current_node.value)
            if current_node.right != None:
                stack.push(current_node.right)
            if current_node.left != None:
                stack.push(current_node.left)
     
    