def isValid(s: str) -> bool:
    stack = []
    
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
            continue
        
        if not len(stack):
            return False

        popped = stack.pop()
            
        if char == ")" and popped != "(":
            return False
        elif char == "]" and popped != "[":
            return False
        elif char == "}" and popped != "{":
            return False
        
    return len(stack) == 0