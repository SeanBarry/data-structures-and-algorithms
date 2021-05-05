using namespace std;
#include <vector>

// O(n) where n is the length of the array | O(1)
bool isValidSubsequence(vector<int> array, vector<int> sequence)
{
	// Store a pointer to the character that's being tested in the sequence
	int current = 0;

	// iterate over the array
	for (int value : array)
	{
		// if the current character is equal to the character
		// in the sequence that is being tested, increment the counter
		if (sequence[current] == value)
		{
			current++;
		}

		// if at any point the counter is the same length as the sequence
		// it means that every char in the sequence is also in the array
		if (current == sequence.size())
		{
			return true;
		}
	}
	return false;
}
