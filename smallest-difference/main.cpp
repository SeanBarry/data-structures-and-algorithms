#include <vector>
using namespace std;

vector<int> smallestDifference(vector<int> arrayOne, vector<int> arrayTwo) {
	sort(arrayOne.begin(), arrayOne.end());
	sort(arrayTwo.begin(), arrayTwo.end());
	
	
  int pointerOne = 0;
	int pointerTwo = 0;
	int smallest = INT_MAX;
	int current = INT_MAX;
	vector<int> smallestPair;
	
	while (pointerOne < arrayOne.size() && pointerTwo < arrayTwo.size()) {
		int first = arrayOne[pointerOne];
		int second = arrayTwo[pointerTwo];
		
		if (first < second) {
			current = second - first;
			pointerOne++;
		} else if (second < first) {
			current = first - second;
			pointerTwo++;
		} else {
			return {first, second};
		}
		
		if (current < smallest) {
			smallest = current;
			smallestPair = { first, second };
		}
	}
	
	return smallestPair;
}