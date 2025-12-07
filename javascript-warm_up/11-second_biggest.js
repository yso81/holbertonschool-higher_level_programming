#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(arg => parseInt(arg));
  
  integers.sort((a, b) => b - a);
  
  console.log(integers[1]);
}