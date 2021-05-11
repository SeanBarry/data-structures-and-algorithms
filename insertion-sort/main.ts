const swap = (i: number, j: number, array: number[]) => {
  let temp = array[j];
  array[j] = array[i];
  array[i] = temp;
};

const insertionSort = (array: number[]) => {
  for (let i = 1; i < array.length; i++) {
    let j = i;

    while (j > 0 && array[j] < array[j - 1]) {
      swap(j, j - 1, array);
      j--;
    }
  }

  return array;
};

export {};
