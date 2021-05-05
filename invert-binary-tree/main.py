class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
	if tree is None:
		return

    left = tree.left
	right = tree.right
	tree.left = right
	tree.right = left
	
	invertBinaryTree(tree.right)
	invertBinaryTree(tree.left)


