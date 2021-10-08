def addBinary(a, b):
    # initialise a carry variable
    carry = 0

    # set up two pointers, both at the right hand side of the input strings
    i = len(a) - 1
    j = len(b) - 1

    # initialise a results variable
    result = ""
    
    # while there are digits left to be processed in a or b
    while i >= 0 or j >= 0:
        # initialise the sum to the value of carry. 0 to begin with
        sum = carry
        # take the char at element i and j of each input string, convert it to a number
        # if you've reached the left of the string (index is 0) then set a default value of
        # 0 as this won't affect the maths
        numA = int(a[i]) if i >= 0 else 0
        numB = int(b[j]) if j >= 0 else 0
        
        # sum up the two chars (carry has been added as sum was initialise to carry's value)
        sum += numA + numB

        # the new carry is sum floor divided by 2.
        # this will be 0 if sum is 0 or 1, but will be 1 if sum is 2
        carry = sum // 2
        # update sum to be sum % 2. this will be 0 if sum is 0, 1 if sum is 1
        # and 0 if sum is 2
        sum = sum % 2

        # convert the sum back to a str and concatenate it to the start of the result string
        result = str(sum) + result
        # decrement both pointers
        i -= 1
        j -= 1

    # once the while loop has exited, the carry variable may have a value of 1 still
    # so we need to concatenate it too. We only want to do this if it has a value though,
    # otherwise we may end up with an unnecessary leading 0
    if carry > 0:
        result = str(carry) + result
        
    return result
        
        
        