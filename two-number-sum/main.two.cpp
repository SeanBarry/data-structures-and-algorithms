#include <vector>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  int leftIdx = 0;
	int rightIdx = array.size() - 1;
	sort(array.begin(), array.end());
  
	while (leftIdx < rightIdx) {
		int currentSum = array[leftIdx] + array[rightIdx];
		
		if (currentSum == targetSum) {
			return {array[leftIdx], array[rightIdx]};
		} else if (currentSum < targetSum) {
			leftIdx++;
		} else if (currentSum > targetSum) {
			rightIdx--;
		}
	}
	return {};
}
