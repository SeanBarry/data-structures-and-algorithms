const smallestDifference = (arrayOne: number[], arrayTwo: number[]) => {
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);

  let pointerOne = 0;
  let pointerTwo = 0;
  let smallest = Infinity;
  let current = Infinity;
  let smallestPair: number[] = [];

  while (pointerOne < arrayOne.length && pointerTwo < arrayTwo.length) {
    let firstNum = arrayOne[pointerOne];
    let secondNum = arrayTwo[pointerTwo];

    if (firstNum < secondNum) {
      current = secondNum - firstNum;
      pointerOne++;
    } else if (secondNum < firstNum) {
      current = firstNum - secondNum;
      pointerTwo++;
    } else {
      return [firstNum, secondNum];
    }

    if (current < smallest) {
      smallest = current;
      smallestPair = [firstNum, secondNum];
    }
  }

  return smallestPair;
};

export {};
