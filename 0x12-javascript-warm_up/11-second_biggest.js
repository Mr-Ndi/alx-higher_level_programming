#!/usr/bin/node

const nums = process.argv.slice(2);

function secB (nums) {
  if (nums.length < 2) {
    return 'Not enough numbers to find the second largest.';
  }

  let max = parseInt(nums[0]);
  let max2 = parseInt(nums[1]);

  for (let i = 2; i < nums.length; i++) {
    const curr = parseInt(nums[i]);

    if (curr > max) {
      max2 = max;
      max = curr;
    } else if (curr > max2 && curr !== max) {
      max2 = curr;
    }
  }

  return max2;
}

const result = secB(nums);
console.log(result);
