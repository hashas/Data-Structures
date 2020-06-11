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
        # if there's no existing head, set head to the given node
        new_node = ListNode(value) # do I need "None, None" ????
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # set the new node's 'next' to the current head
            new_node.next = self.head
            # set the current head's 'prev' to the new node
            self.head.prev = new_node
            # reassign self.head (current head) to the new node
            # this preferrably is last step so we don't lose direct
            # access to the two nodes before reassigning
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        # this is the delete method contained in this class (not from Node method)
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # this will be similar/mirror add_to_head()
        # generally this is more mirroring with doubly vs singly LL
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            # set the new node's 'prev' to the current tail
            new_node.prev = self.tail
            # set the current tail's next to the new node
            self.tail.next = new_node
            # reassign the self.tail (current tail) to the new node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # similar to remove_from_head()
        value = self.head.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # check if the node is the head
        if node is self.head:
            return None
        # store a reference to the node we're about to delete/move
        # store the value of the node so we can use add_to_head() method below
        value = node.value
        # let's check if node is tail because we aleady have .remove_from_tail()
        # method we can use
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        # add_to_head() method takes a value (not a node) so amend value
        # variable above to value = node.value
        self.add_to_head(value)
        # set the node which saved before deleting as the new head
        # (i.e. move to the front)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # similar to move_to_front()
        if node is self.tail:
            return None
        # store reference to node we're about to delete/move
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        # "is" in python is "===" in js i.e. are 2 vars pointing at same spot in memory
        # remove that one single node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # check if the node is the head of the list, if so we'll need to move the head
        # reference to the current head's (the one we're deleting) next node
        elif self.head is node:
            # set head to the 'next' of the node we're deleting
            # we need to do this before we delete the node otherwise we lose access to it
            self.head = node.next
            node.delete()
        # check similar thing for tail
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # otherwise, there's no additional references we need to update
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # initialize a variable that will keep track of the largest elements we've
        # seen so far
        current_max = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            current = current.next
        return current_max

