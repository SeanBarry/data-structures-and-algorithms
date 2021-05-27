#include <vector>
#include <unordered_set>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  unordered_set<int> nums;
	
	for (int num = 0; num < array.size(); num++) {
		int unknown = targetSum - array[num];
		
		if (nums.find(unknown) != nums.end()) {
			return {unknown, array[num]};
		} else {
			nums.insert(array[num]);
		}
	}
  return {};
}
