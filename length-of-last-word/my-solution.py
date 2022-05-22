def lengthOfLastWord(s):
    # set a pointer at the end of the string
    pointer = len(s) - 1
    
    # track if letters have been encountered, or if only spaces
    has_hit_letters = False
    # count the number of letters encountered
    number_of_letters = 0
    
    # iterate from the end of the string
    while pointer >= 0:
        # grab the current character
        current = s[pointer]
        
        # if the current character is a letter
        if current != " ":
            # record that we have hit a letter (may already be true)
            has_hit_letters = True
            # increment the number of letters that we've hit
            number_of_letters += 1
            # decrement the pointer to move to the next character
            pointer -= 1
            # restart the logic in the while loop
            continue
        
        # if the current character is a space:
        if current == " ":
            # if we haven't yet hit any letters, then 
            # we can continue as the end of the string had spaces
            if has_hit_letters == False:
                pointer -= 1
                continue
            else:
                # if however we already had hit letters but are now hitting
                # a space, it means we have consumed an entire word & can
                # return its length
                break
            
    # we've exited the loop, so time to return the longest word length
    return number_of_letters
            
        
                