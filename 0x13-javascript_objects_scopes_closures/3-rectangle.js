#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let sn = '';
      for (let g = 0; g < this.width; g++) {
        sn += 'x';
      }
      console.log(sn);
    }
  }
}
module.exports = Rectangle;
