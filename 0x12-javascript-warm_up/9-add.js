#!/usr/bin/node

const args = process.argv.slice(2);

function add(a, b) {
  a = Number(args[0]);
  b = Number(args[1]);
  let sum = a + b;
  return (sum);
}
console.log(add());
