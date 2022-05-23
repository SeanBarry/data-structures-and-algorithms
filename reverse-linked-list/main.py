class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


def reverseLinkedList(head):
	# Set a pointer to the current and the previous nodes
	current = head
	prev = None

	while current is not None:
		# store the next node as a temp
		next = current.next
		# update the current's next to point to the previous
		current.next = prev
		# slide the pointers along by one node
		prev = current
		current = next
	# the while loop ends when current is None
	# so the prev will be the new head of the LL
	return prev
		