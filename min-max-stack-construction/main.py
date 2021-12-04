class MinMaxStack:
    # initialise the stack and the cache for min/max
    def __init__(self):
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        # return the last element in the stack
        return self.stack[len(self.stack) - 1]

    def pop(self):
        # remove the last min/max cached value
        self.min_max_stack.pop()
        # return the last element in the stack
        return self.stack.pop()
        
    def push(self, number):
        # create a hashmap of min/max
        new_min_max = { "min": number, "max": number }

        # if there are values in the stack, update the min/max to the actual 
        # min/max using the built in methods
        if len(self.stack):
            last_min_max = self.min_max_stack[len(self.min_max_stack) - 1]
            new_min_max["min"] = min(last_min_max["min"], number)
            new_min_max["max"] = max(last_min_max["max"], number)
        # append to the min/max cache 
        self.min_max_stack.append(new_min_max)
        # append the number to the stack
        self.stack.append(number)
            
    # return the min value at the latest point in the cache
    def getMin(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]["min"]

    # return the max value at the latest point in the cache
    def getMax(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]["max"]
