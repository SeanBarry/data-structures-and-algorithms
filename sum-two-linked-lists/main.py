class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Create a dummy linked list
    new_linked_list_head_pointer = LinkedList(0)
    # Set the current node to the linked list pointer
    current_node = new_linked_list_head_pointer
    # initialise a carry variable as 0
    carry = 0

    node_one = linkedListOne
    node_two = linkedListTwo

    # execute while either node is not null or the carry doesn't equal 0
    while node_one is not None or node_two is not None or carry != 0:
        # get the values, default to 0 if there is no value
        value_one = node_one.value if node_one is not None else 0
        value_two = node_two.value if node_two is not None else 0

        # calculate the sum of the values (including any carry)
        sum_values = value_one + value_two + carry

        # By modding the sum_values by 10, the remainder is the least significant digit
        # E.G sum_values is 15, new_value will be 5
        new_value = sum_values % 10
        # We then create a new LinkedList node with the new_value as its value
        new_node = LinkedList(new_value)
        # We add this new node as the .next of the current node
        current_node.next = new_node
        # We then made the current node the new one that we just added
        current_node = new_node

        # We use integer division (floor division) to work out what the carry is
        # E.G if sum_values is 18, then carry will be 1 (18 / 10) -> rounded down
        carry = sum_values // 10

        # Finally we can increment the nodes and set them to None by default
        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None


    # The last step is to return the .next LinkedList node of our dummy LL because it was
    # initiated as 0
    return new_linked_list_head_pointer.next