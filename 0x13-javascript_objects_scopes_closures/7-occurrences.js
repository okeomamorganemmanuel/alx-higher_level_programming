#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let index = 0;
  list.forEach((element) => {
    if (element === searchElement) {
      index++;
    }
  });
  return index;
};
