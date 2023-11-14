#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let character = '';
    for (let j = 0; j < this.height; j++) {
      character = '';
      for (let i = 0; i < this.width; i++) {
        character += 'X';
      }
      console.log(character);
    }
  }
}

module.exports = Rectangle;
