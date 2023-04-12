#!/usr/bin/node

const argx = process.argv.slice(2);

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

let factor;

if (!isNaN(parseInt(argx[0]))) {
  factor = factorial(parseInt(argx[0]));
  console.log(factor);
} else {
  factor = 1;
  console.log(factor);
}
