#!/usr/bin/node

const myInt = process.argv.slice(2);

const numb = Number(myInt[0]);
if (isNaN(myInt) || !numb) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + myInt);
}
