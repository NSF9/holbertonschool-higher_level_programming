#!/usr/bin/node
const integersList = process.argv.reduce((acc, c) => {
  const int = [Number.parseInt(c, 10)];
  if (!isNaN(int[0])) {
    return acc.concat(int);
  }
  return acc;
}, []);
const secondLastOrZero = (list) => {
  if (list.length < 2) {
    return 0;
  }
  return list[list.length - 2];
};
integersList.sort((a, b) => a - b);
console.log(secondLastOrZero(integersList));
