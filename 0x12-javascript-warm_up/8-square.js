#!/usr/bin/node
const sig = process.argv[2];
const num = parseInt(sig);
if (isNaN(sig) || !sig) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  let ans = '';
  for (let j = 0; j < num; j++) {
    ans += 'X';
  }
  console.log(ans);
}
