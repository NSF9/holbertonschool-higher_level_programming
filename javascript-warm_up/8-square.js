#!/usr/bin/node
const x = Number.parseInt(process.argv[2], 10);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
