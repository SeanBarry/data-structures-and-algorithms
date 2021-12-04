def nextGreaterElement(array):
    # fill a results array the same length as the input array with -1
    results = [-1] * len(array)
    # initialise a stack
    stack = []

    # iterate over the array twice
    for i in range(len(array) * 2):
        # modulo the index of the array by the length of the array
        # so we can iterate over it a second time
        idx = i % len(array)
        
        # while there are items in the stack, and the current array item
        # is greater than the top of the stack
        while len(stack) > 0 and array[idx] > array[stack[-1]]:
            # grab the item at the top of the stack
            top = stack.pop()
            # set the results array at the index of the popped item to the value
            # of the current array item
            results[top] = array[idx]

        # push the current array index onto the stack
        stack.append(idx)

    # return the results array
    return results
            
        
