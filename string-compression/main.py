def compress_string(chars):
    # set up a var to track the index of the results array
    index = 0
    # set a pointer initialised to 0
    i = 0
    
    # loop through the chars array, staying in bounds
    while i < len(chars):
        # set a pointer to the current char
        j = i
        
        # loop through the chars array, staying in bounds, and incrementing the pointer
        # when the current char is the same as the next char
        while j < len(chars) and chars[j] == chars[i]:
            j += 1
            
        # when the while above breaks, we can insert the current char
        # in the results array, then increment the index
        chars[index] = chars[i]
        index += 1
        
        # we only need to "compress" it if there is more than one of the chars
        # so if j - 1 > 1, then do the compression
        if j - i > 1:
            # whatever the difference in value is between the two pointers is the number of times
            # that the char was repeated. Convert it to a string
            count = str(j - i)
            # insert the digits of the count in to the results array, one by one
            for letter in count:
                chars[index] = letter
                index += 1
        
        # lastly set the pointer to the next char
        i = j
    
    # return the index, which is the length of the "results"
    return index
        