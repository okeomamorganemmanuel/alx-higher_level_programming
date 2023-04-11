#!/usr/bin/node

const argx = process.argv.slice(2);

if (!isNaN(parseInt(argx[0]))) {
  let num = parseInt(argx[0]);

  while (num > 0) {
    console.log('C is fun');
    num--;
  }
} else {
  console.log('Missing number of occurence');
}
