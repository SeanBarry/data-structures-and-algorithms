class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
	# if there is no tree, don't go any further
	if tree is None:
		return None

	# swap the children
	temp = tree.left
	tree.left = tree.right
	tree.right = temp
	
	# recursively call the method on the children
	invertBinaryTree(tree.right)
	invertBinaryTree(tree.left)

	# be sure to return the tree
	return tree
