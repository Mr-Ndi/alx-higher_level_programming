#!/usr/bin/node
const arg = process.argv;

if (!arg[2]) {
  console.log('No argument');
} else if (!arg[3]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
