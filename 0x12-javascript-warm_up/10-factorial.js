#!/usr/bin/node

const firstArgs = process.argv.slice(2);
const numb = Number(firstArgs[0]);

function factorial(n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(numb));
