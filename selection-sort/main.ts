const swap = (i, j, array) => {
  let temp = array[j];
  array[j] = array[i];
  array[i] = temp;
};

const selectionSort = (array) => {
  let currentIdx = 0;

  while (currentIdx < array.length - 1) {
    let smallestIdx = currentIdx;

    for (let i = currentIdx + 1; i < array.length; i++) {
      if (array[i] < array[smallestIdx]) {
        smallestIdx = i;
      }
    }

    swap(currentIdx, smallestIdx, array);
    currentIdx++;
  }

  return array;
};

// fix ts export bugs
export {};