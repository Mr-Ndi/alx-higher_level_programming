#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
function fact (num1) {
  if (isNaN(num1) || num1 < 0 || num1 === 1 || num1 === 0) {
    return 1;
  } else {
    return (num1 * fact(num1 - 1));
  }
}
console.log(fact(num1));
