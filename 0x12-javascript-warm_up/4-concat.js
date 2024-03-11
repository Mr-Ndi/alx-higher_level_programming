#!/usr/bin/node
const arg = process.argv;

if (!arg[2]) {
  console.log('undefined is undefined');
} else if (!arg[3]) {
  console.log(arg[2], 'is undefined');
} else {
  console.log(arg[2], 'is', arg[3]);
}
