export function sortedSquaredArray(array: number[]) {
  // init new array of same length full of zeroes
  const results = new Array(array.length).fill(0);
  // set pointers to right and left
  let leftPointer = 0;
  let rightPointer = array.length - 1;

  // looping from right to left of results array
  for (let idx = array.length - 1; idx >= 0; idx--) {
    // grab the actual values from the input pointers
    const smallerValue = array[leftPointer];
    const largerValue = array[rightPointer];
    // if the larger value is greater, square it, place it
    // at the idx and then decrease the rightPointer
    if (Math.abs(largerValue) > Math.abs(smallerValue)) {
      results[idx] = largerValue * largerValue;
      rightPointer--;
    } else {
      // otherwise square the left pointer value and place it at the
      // index and increase the left Pointer
      results[idx] = smallerValue * smallerValue;
      leftPointer++;
    }
  }

  return results;
}

export {};
