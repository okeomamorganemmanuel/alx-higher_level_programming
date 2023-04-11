#!/usr/bin/node

const argx = process.argv.slice(2);

if (isNaN(argx)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argx; i++) {
    let row = '';
    for (let j = 0; j < argx; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
