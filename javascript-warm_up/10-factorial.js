#!/usr/bin/node
function factorial (x) {
  if (x === 1 || x === 0 || isNaN(x)) {
    return 1;
  }
  return factorial(x - 1) * x;
}
const x = Number.parseInt(process.argv[2], 10);
console.log(factorial(x));
