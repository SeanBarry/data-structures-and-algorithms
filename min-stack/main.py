class MinStack:
    # initialise the stack and min stack
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        # append the value to the stack
        self.stack.append(val)
        # need to check if the minStack is empty, otherwise
        # the search for the last element will throw an error
        if self.minStack:
            # add the minimum of the current minimum
            # and the new value to the min stack
            val = min(self.minStack[-1], val)
        self.minStack.append(val)

    # rest is self explanatory
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
