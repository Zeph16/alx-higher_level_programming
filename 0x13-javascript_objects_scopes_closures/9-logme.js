#!/usr/bin/node
exports.logMe = (function (item) {
  let count = 0;
  const clousure = (item) => {
    console.log(`${count}: ${item}`);
    count+= 1;
  };
  return clousure;
}());
