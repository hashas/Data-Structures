# this was my attempt prior to watching day2 lecture video
# I have since implemented an updated version of linked_list.py
# in the ../stack/ and ../queue/

# this Node class only knows its value and the next value
class Node:
	def __init__(self, value=None, next_node=None)
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

# this LinkedList class represents the list, it has a head and tail, and some
# functions which add/remove nodes
class LinkedList:
	def __init__(self):
		# first node in the list
		self.head = None
		# last node in the list
		self.tail = None

	# S.Chen implemented this differently in Day 2 guided
	def add_last(self, value):
		# regardless if list is empty, we need to wrap value with Node
		new_node = Node(value)
		# if the list is empty, set new node as head:
		if not self.head:
			self.head = new_node
			self.tail = new_node
		# if the list isn't empty:
		else:
			# traverse all the nodes, starting from head, looking for first node
			# which has an empty 'next_node'
			current = self.head
			# while 'next_node' is not empty, store that 'next_node' to a variable 
			# 'current', and loop again
			while current.get_next() is not None:
				current = current.get_next()
			# while loop ends when we reach a node with a 'next_node' which is empty, at which point
			# we've reach the end of the linked list - this node which doesn't have a next_node will 
			# assigned to the tail (in LinkedList object)
			# so set self.tail to 'current'
			self.tail = current
			# the new_node will be set as the 'next_node'
			# whatever current node the loop ends at (the one that doesn't have 'next_node'), we now  
			# need to make 'new_node' it's 'next_node' 
			current.set_next(new_node)

	def remove_from_head(self):
		# if the list is empty:
		if not self.head:
			return None
		# what if list isn't empty
		else:
		# return the value at the current head for safekeeping before you remove it
		value = self.head.get_value()
		# update the value at the head to the 'next_node' of the head we're removing
		self.head = self.head.get_next()
		return value

	def remove_from_tail(self):
		# if the list is empty
		if not self.head:
			return None
		# if the list isn't empty
		else:
			# use these variables to determine relative position in the while loop
			previous = self.head
			current = self.head
			while current.get_next() is not None:
				# if current does have a 'next_node', store it in a variable for later reference
				previous = current
				# if current does have a 'next_node', update 'current' variable to the next node
				# and continue loop
				current = current.get_next()
			# loop ends when we reach a node with an empty 'next_node'
			# that is the last node which we want to remove
			# we do this by setting 'next_node' insdie 'previous' to null/None
			previous.set_next(None)
			# return the deleted tail value
			return current.value

	def new_head(self, value):
		pass

	def remove_head(self):
		pass