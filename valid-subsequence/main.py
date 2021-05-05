def isValidSubsequence(array, sequence):
    # Write your code here.
	current = 0
	
	for num in array:
		if (num == sequence[current]):
			current += 1
		
		if current == len(sequence):
			return True
	
	return False;
