#!/usr/bin/node
const sig = process.argv[2];
const num = parseInt(sig);
if (!sig) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
