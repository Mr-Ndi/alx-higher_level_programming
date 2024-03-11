#!/usr/bin/node

const nums = process.argv.slice(2);

function secB (nums) {
  if (!nums[0] || nums[0] === '1' || nums[0] === '0') {
    return 0;
  } else {
    let max = parseInt(nums[0]);
    let max2 = parseInt(nums[0]);
    for (let i = 0; i < nums.length; i++) {
      const curr = parseInt(nums[i]);
      if (max < curr) {
        max2 = max;
        max = curr;
      }
    }
    return max2;
  }
}

const result = secB(nums);
console.log(result);
