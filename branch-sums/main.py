class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSumsHelper(tree, sum, results):
    if tree.left:
        branchSumsHelper(tree.left, sum + tree.value, results)

    if tree.right:
        branchSumsHelper(tree.right, sum + tree.value, results)

    if tree.left is None and tree.right is None:
        results.append(sum + tree.value)


def branchSums(root):
    results = []
    branchSumsHelper(root, 0, results)
    return results
