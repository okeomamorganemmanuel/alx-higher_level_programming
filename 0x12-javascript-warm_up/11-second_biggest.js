#!/usr/bin/node

const argx = process.argv.slice(2);

if (argx.length === 0 || argx.length === 1) {
  console.log(0);
} else {
  argx.sort((a, b) => b - a);
  console.log(parseInt(argx[1]));
}
