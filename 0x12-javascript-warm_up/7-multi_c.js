#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = Number(args[0]);

if (args.length !== 1 || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
