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

type StackItem = {
  node: BinaryTree | null;
  depth: number;
};

export function nodeDepths(root: BinaryTree) {
  let sumOfDepths = 0;
  let stack: StackItem[] = [{ node: root, depth: 0 }];

  while (stack.length) {
    let nodeInfo = stack.pop();

    if (!nodeInfo) {
      continue;
    }

    let { node, depth } = nodeInfo;

    if (!node) {
      continue;
    }

    sumOfDepths += depth;

    stack.push({ node: node.left, depth: depth + 1 });
    stack.push({ node: node.right, depth: depth + 1 });
  }

  return sumOfDepths;
}

export {};
