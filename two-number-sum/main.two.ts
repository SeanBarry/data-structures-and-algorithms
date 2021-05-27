// O(n log(n)) time | O(1) space

const twoNumberSum = (array: number[], targetSum: number) => {
	array.sort((a, b) => a - b);
	let leftIdx = 0;
	let rightIdx = array.length - 1;

	while (leftIdx < rightIdx) {
		const currentSum = array[leftIdx] + array[rightIdx];
		if (currentSum === targetSum) {
			return [array[leftIdx], array[rightIdx]];
		} else if (currentSum < targetSum) {
			leftIdx++;
		} else if (currentSum > targetSum) {
			rightIdx--;
		}
	}

	return [];
};

export {};
