class Node:
	def __init__(self, value=None, next_node=None):
		# teh value at this linked list node
		self.value = value
		# reference to the next node in the list
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		# set this node's next_node to the passed in node
		self.next_node = new_next

class LinkedList:
	def __init__(self):
		# first node in the list
		self.head = None
		# last node in the list
		self.tail = None

	# O(1)
	def add_to_head(self, value):
		new_node = Node(value)

		if not self.head and not self.tail:
			self.head = new_node
			self.tail = new_node
		else:
			# in order to make 'new_node' the new head we must
			# set its 'next_node' to the current head
			new_node.set_next(self.head)
			# then set self.head to 'new_node'
			self.head = new_node

	# we have access to the end of the list so we can directly add new nodes to it
	# O(1)
	def add_to_end(self, value):
		new_node = Node(value)
		# what if list is empty?
		if not self.head and not self.tail:
			# set both self.head and self.tail to 'new_node'
			self.head = new_node
			self.tail = new_node
		# what if list isn't empty
		else:
			# set next node of current tail to 'new_node'
			self.tail.set_next(new_node)
			# set self.tail to 'new_node'
			self.tail = new_node

	# the above two methods are enough to implement Queues (FIFO, add from one
	# side and remove from the other side)

	# to implement Stacks (LIFO, we must add & remove from same side) we need to
	# add one more method

	# we already have access to the head of the linked list, so we can directly 
	# remove from it
	# O(1)
	def remove_from_head(self):
		# if the list is empty, nothing to remove
		if not self.head:
			None
		# if the list is not empty
		else:
			# return the value of the current head before we lose it forever
			value = self.head.get_value()
			# remove the node at the head, set self.head to current head's 'next_node'
			self.head = self.head.get_next()
			return value

