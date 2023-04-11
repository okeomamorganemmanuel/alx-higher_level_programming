#!/usr/bin/node

const argx = process.argv.slice(2);

if (!isNaN(parseInt(argx[0]))) {
  const num = 'My number: ' + argx[0];
  console.log(num);
} else {
  console.log('Not a number');
}
