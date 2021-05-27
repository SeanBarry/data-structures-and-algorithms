// O(n) time | O(n) space

const twoNumberSum = (array: number[], targetSum: number) => {
	//create cache
	const hashTable: { [key: string]: boolean } = {};
	// iterate through array
	for (const v of array) {
		// unknown is target minus current iteree
		const unknown = targetSum - v;

		// if unknown is in hashtable, it exists earlier in array
		if (hashTable[unknown]) {
			return [unknown, v];
		} else {
			hashTable[v] = true;
		}
	}

	return [];
};

export {};
