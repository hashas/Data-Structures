"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the current node has a value, if not set it to incoming value
        if not self.value:
            self.value = BSTNode(value)
        # check if the incoming value is less than current node's value
        elif value < self.value:
            # if its less, check if self.left is empty, if so set left to
            # the incoming value 
            if not self.left:
                self.left = BSTNode(value)
            # if self.left is not empty we can't insert here so we need to recurse
            # (i.e. keep searching)
            else:
                return self.left.insert(value)
        # otherweise we need to go right 
        else:
            # check if self.right is empty
            if not self.right:
                # if empty insert the value as a node in the tree here
                self.right = BSTNode(value)
            else:
                # if self.right not empty, we can't insert here so need to recurse
                # (i.e. keep searching)
                self.right.insert(value)

# there are no return statements in insert because we don't have to send anything back up
# although the yo-yoing still holds here, even though we didn't put any return statements
# the code will implicitly return None if we don't specify a return, we still see the yo-yo
# effect as we go back up the tree there's just no message because we didn't specify a return,
# but yoyoing is still happening

# also, why would we return anything when we already have access to the value we're inserting
# from the start!!!              


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            # the recursive calls are moving us through the tree by restarting
            # the function call at the top but with self.left as the current node
            # but carrying forward teh 'target' argument
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check if the current node has a value, if not return None
        if not self.value:
            return None
        # otherwise if self.right is empty, return self.value
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # iterative version of get_max (similar to traversing linked list)
    def iterative_get_max(self):
        current_max = self.value

        # set a 'current' pointer to the current node we're on i.e. self
        current = self
        # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
        # update our current_max variable if we see a larger value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on value of existing node
        fn(self.value)

        if self.left:
            # pass this function to the left child, which will restart this
            # function at the top but now with left child as the current node
            self.left.for_each(fn)
        if self.right:
            # pass this function to the right child
            self.right.for_each(fn)


    def iterative_for_each(self, fn):
        stack = [] 

        # add the root node
        stack.append(self)

        # loop so long as the stack still has elements 
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        # print(node.value)

        if self.left is not None:
            self.left.in_order_print(self.left)
        # when print() was in else, it wasn't print the current node.value when
        # we were on the way back up the recursion calls, obviously because it
        # would only call print() "if there's no left" which in our case there was
        # else:
        #     print(node.value)

        # this way, if there's no self.left this will print current node.value
        # if there is a self. left, it will traverse down the tree, then on the 
        # way back up this whole function runs again, but because that recursive call
        # in the above if statement has already traversed self.left and returned something, 
        # so it will just print current node.value
        print(node.value)

        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()

        # add the root node to queue
        queue.append(node)

        # loop so long as the queue has elements
        while len(queue) > 0:
            # pop the first element (FIFO) in the queue off the queue and assign it
            # to 'current' variable
            current = queue.popleft()
            # if current has a right, add it to the queue
            if current.right:
                queue.append(current.right)
            # if current has a left, add it to the queue
            if current.left:
                queue.append(current.left)

            # print current.value
            print(current.value)
            # now loop to the top


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        # add the root node to stack
        stack.append(node)

        # loop as long as stack has elements
        while len(stack) > 0:
            # pop off the last added element (LIFO) and assign to 'current'
            current = stack.pop()
            # if current has either a left or right, then add them to stack
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

            # print current.value
            print(current.value)
            # now loop back to top

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # i.e. root-left-right: 1, 8, 5, 3, 2, 4, 7, 6
    def pre_order_dft(self, node):
        
        print(node.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    # i.e. left-root-right: 2, 4, 3, 6, 7, 5, 8, 1
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)

        if self.right:
            self.right.post_order_dft(self.right)

        print(node.value)



