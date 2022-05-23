def isPalindrome(s: str) -> bool:
    # create pointers 
    l, r = 0, len(s) - 1
    # this works with < or <= because with the latter 
    # l and r are the same so will always be identical
    while l < r:
        # nested while loop to consume all non alphanumerics on the left
        # NOTE: important to also check l < r or can get index out of
        # range errors
        while l < r and not s[l].isalnum():
            l += 1
        # nested while loop to consume all non alphanumerics on the right
        # NOTE: important to also check l < r or can get index out of
        # range errors
        while l < r and not s[r].isalnum():
            r -= 1
        # now check if the lower case letters are equal, if not return False
        if s[l].lower() != s[r].lower():    
            return False
        # if they are, move both pointers
        l += 1; r -= 1
    
    # string is a palindrome
    return True

