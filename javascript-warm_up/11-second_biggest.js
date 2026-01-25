#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const nums = args.map(x => parseInt(x, 10));
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
