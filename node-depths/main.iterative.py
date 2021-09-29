class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    # initialise the sum of the depths
    sumOfDepths = 0;
    # create a stack with each node and its corresponding depth, ready to be processed
    stack = [{ "node": root, "depth": 0}]
	
    # while there are items in the stack
    while len(stack) > 0:
        # grab a node from the stack
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
		
        if node is None:
            continue

        # increase the depths sum by the depth of the node
        sumOfDepths += depth

        # append the node's children to the stack, incrementing their depth count by 1
        stack.append({ "node": node.left, "depth": depth + 1})
        stack.append({ "node": node.right, "depth": depth + 1})
	
    # once the stack is empty, return the sum of the depths
    return sumOfDepths


