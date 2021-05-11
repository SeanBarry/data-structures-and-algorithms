export function isValidSubsequence(array: number[], sequence: number[]) {
  let current = 0;

  for (let num of array) {
    if (num === sequence[current]) {
      current++;
    }

    if (current === sequence.length) {
      return true;
    }
  }
  return false;
}

export {};
