const radixSort = (array: number[]) => {
  if (array.length === 0) {
    return array;
  }

  const maxNumber = Math.max(...array);

  let maxNumberLength = maxNumber.toString().length;

  for (let i = 0; i < maxNumberLength; i++) {
    countingSort(array, i);
  }

  return array;
};

const countingSort = (array: number[], digit: number) => {
  // create empty array of same length as data array
  const sortedArray = new Array(array.length).fill(0);
  // create empty array with same num unique digits as base number system
  const countArray = new Array(10).fill(0);

  const digitColumn = 10 ** digit;

  for (const num of array) {
    // iterate over the array and increment the column of the digit being sorted
    const countIndex = Math.floor(num / digitColumn) % 10;
    countArray[countIndex]++;
  }

  // add previous index count to each count such that the result is the earliest
  // index each number can be placed in the sorted array
  for (let idx = 1; idx < 10; idx++) {
    countArray[idx] += countArray[idx - 1];
  }

  // iterate over the array backwards, decrement the countArray value for each number
  // and place the number in the index from the countArray
  for (let idx = array.length - 1; idx > -1; idx--) {
    const countIndex = Math.floor(array[idx] / digitColumn) % 10;
    countArray[countIndex]--;
    const sortedIndex = countArray[countIndex];
    sortedArray[sortedIndex] = array[idx];
  }

  // convert the original array to the sorted array
  for (let idx = 0; idx < array.length; idx++) {
    array[idx] = sortedArray[idx];
  }
};

export {};
