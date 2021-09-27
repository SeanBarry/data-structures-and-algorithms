class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


def removeNthNodeFromEnd(head, n):
	# set a first and second pointer to the head node
	first = head
	second = head
	# initialise a counter set to 1
	counter = 1

	# while the counter is <= n, increment the second pointer and the counter variable
	while counter <= n:
		second = second.next
		counter += 1

	# when we break out of this while, second will be n nodes ahead of first    
	# second is already none so first is the head of the LL
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		# make sure to return because we do not want to do anything else
		return

	# this explicitly checks that second.next is not None. This means that when the while loop breaks
	# second will be the last node and first will be the node before the one we wish to remove
	while second.next is not None:
		second = second.next
		first = first.next
		
	# move the first nodes pointer to its next.next value to remove the nth node
	first.next = first.next.next
		
		
