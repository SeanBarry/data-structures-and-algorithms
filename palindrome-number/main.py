def isPalindrome(number):
    # Negative numbers can't be palindromes because of the negative sign
    if number < 0:
        return False

    # convert the number to a string (prob not optimal)
    stringNumber = str(number)

    # create left and right pointers
    right = len(stringNumber) - 1
    left = 0
    
    # while the pointers haven't crossed
    while left < right:
        # if the values at each pointers are equal, move them
        if stringNumber[left] == stringNumber[right]:
            left += 1
            right -= 1
        else:
            # otherwise the values are different so return false
            return False

    # when the while loop executes without returning false, return true       
    return True
     