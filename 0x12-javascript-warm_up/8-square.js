#!/usr/bin/node

const args = process.argv.slice(2);

const firstArg = Number(args[0]);
let square = '';

if (!firstArg || isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    square = '';
    for (let j = 0; j < firstArg; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
