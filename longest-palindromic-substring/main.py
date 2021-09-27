def longestPalindromicSubstring(string):
	currentLongest = [0, 1]

for i in range(1, len(string)):
	# check odd and even length palindromes
	odd = getLongestPalindromFrom(string, i - 1, i + 1)
	even = getLongestPalindromFrom(string, i - 1, i)

	# pick the longest of the odd/even results
	longest = max(odd, even, key=lambda x: x[1] - x[0])
	# set the currentLongest to the largest of the longest or the recorded longest
	currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])

	# slice the string to return the longest palindrome. Have to +1 to the second val as range it's exclusive
	return string[currentLongest[0] : (currentLongest[1] + 1)]

# Helper function to return the longest palindrome in a string
def getLongestPalindromFrom(string, leftIdx, rightIdx):
	# Loop while the pointers are in bounds
	while leftIdx >= 0 and rightIdx < len(string):
		# If left val != right val, break loop
		if string[leftIdx] != string[rightIdx]:
			break

	# If they are equal, move the pointers to test more characters
	leftIdx -= 1
	rightIdx += 1

	# when the loop breaks, the pointers have moved past the last characters that are the same
	return [leftIdx + 1, rightIdx - 1]
