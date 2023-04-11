#!/usr/bin/node

const argx = process.argv.slice(2);

if (!argx[0]) {
  console.log('No argument');
} else if (argx.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
