const isMonotonic = (array: number[]) => {
  let start = array[0];
  let end = array[array.length - 1];
  let trendingUp = end > start;

  if (array.length < 2) {
    return true;
  }

  for (let i = 1; i < array.length; i++) {
    if (trendingUp && array[i] < array[i - 1]) {
      return false;
    } else if (!trendingUp && array[i] > array[i - 1]) {
      return false;
    }
  }

  return true;
};

export {};
