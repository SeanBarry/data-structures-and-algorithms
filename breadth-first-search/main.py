class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # create a queue and add the node to the queue
        queue = [self]

        # iteratively - while the queue has items in it
        while len(queue) > 0:
            # pop the item at the START of the queue (this is very important)
            current = queue.pop(0);

            # add the item to the results
            array.append(current.name)

            # then add the item's children to the END of the queue
            for child in current.children:
                queue.append(child)
        
        return array
