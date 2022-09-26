# define the corresponding parenthesis sets
parenthesis_mapping = {
    "{": "}",
    "[": "]",
    "(": ")"
}

def isValid(s: str) -> bool:
    # initialise a stack
    stack = []
    
    for char in s:
        # if the character is an opening parenthesis, append it to the stack
        # and move on
        if char in ["(", "[", "{"]:
            stack.append(char)
            continue
        
        # otherwise, if the stack is empty then it's an invalid string
        if not len(stack):
            return False

        # if the stack isn't empty, grab the last item
        popped = stack.pop()

        # if the character isn't the corresponding parenthesis to the latest item
        # in the stack, the string is invalid
        if char != parenthesis_mapping[popped]:
            return False
    
    # when we finish iterating the string, the stack may still have unclosed opening parenthesis
    # in it. E.G. if the input string is: "(((())"
    # As such, we want to return True only if the stack is empty, otherwise the string is invalid.
    return len(stack) == 0