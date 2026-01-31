#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const x = Number.parseInt(process.argv[2], 10);
const y = Number.parseInt(process.argv[3], 10);
console.log(add(x, y));
