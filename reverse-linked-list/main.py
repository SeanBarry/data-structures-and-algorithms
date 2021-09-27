class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


def reverseLinkedList(head):
	# Set a pointer to the current and the previous nodes
	current = head
	prev = None

	while current is not None:
		next = current.next
		current.next = prev
		prev = current
		current = next

	return prev
		