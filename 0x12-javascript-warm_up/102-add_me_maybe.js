#!/usr/bin/node

exports.addMeMaybe = function (number, f) {
  number++;
  f(number);
};
