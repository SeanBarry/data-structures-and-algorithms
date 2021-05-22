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

const branchSumsHelper = (tree: BinaryTree, sum: number, results: number[]) => {
  if (tree.left) {
    branchSumsHelper(tree.left, sum + tree.value, results);
  }

  if (tree.right) {
    branchSumsHelper(tree.right, sum + tree.value, results);
  }

  if (!tree.left && !tree.right) {
    results.push(sum + tree.value);
  }
};

export function branchSums(root: BinaryTree): number[] {
  const results: number[] = [];

  branchSumsHelper(root, 0, results);

  return results;
}

export {};
