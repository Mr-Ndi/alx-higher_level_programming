#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
if (!num1 || !num2) {
  console.log('NaN');
} else {
  console.log(num1 + num2);
}
