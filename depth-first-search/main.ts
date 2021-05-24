export class Node {
  name: string;
  children: Node[];

  constructor(name: string) {
    this.name = name;
    this.children = [];
  }

  addChild(name: string) {
    this.children.push(new Node(name));
    return this;
  }

  depthFirstSearch(array: string[]) {
    // push the node in to the results
    array.push(this.name);

    // for each child, call recursively call this method
    for (let child of this.children) {
      child.depthFirstSearch(array);
    }

    return array;
  }
}
