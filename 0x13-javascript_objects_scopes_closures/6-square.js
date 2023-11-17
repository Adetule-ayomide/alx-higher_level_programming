#!/usr/bin/node

const firstSquare = require('./5-square');

class Square extends firstSquare {
  charPrint (c) {
    const charprint = c || 'X';
    let character = '';
    for (let j = 0; j < this.height; j++) {
      character = '';
      for (let i = 0; i < this.width; i++) {
        character += charprint;
      }
      console.log(character);
    }
  }
}
module.exports = Square;
