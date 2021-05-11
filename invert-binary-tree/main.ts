class BinaryTree {
  value: number;
  left: BinaryTree | null;
  right: BinaryTree | null;

  constructor(value: number) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
/**
 * Recursive Solution - O(n) time | O(d) space where d = depth
 */
export const invertBinaryTree = (tree: BinaryTree | null) => {
  // If we reach the end of a branch
  if (!tree) {
    return;
  }

  // swap out left and right
  let right = tree.right;
  let left = tree.left;
  tree.right = left;
  tree.left = right;

  // recursively call the function on the right/left branches.
  // If they are null this is handled by the check on line 15
  invertBinaryTree(tree.right);
  invertBinaryTree(tree.left);
};

export {};
