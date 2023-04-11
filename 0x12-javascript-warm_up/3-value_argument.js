#!/usr/bin/node

const argx = process.argv.slice(2);

if (!argx[0]) {
  console.log('No argument');
} else if (argx[0]) {
  console.log(argx[0]);
}
