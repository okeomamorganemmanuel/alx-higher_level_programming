#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const userId in dict) {
  const occurence = dict[userId];
  if (occurence in newDict) {
    newDict[occurence].push(userId);
  } else {
    newDict[occurence] = [userId];
  }
}
console.log(newDict);
