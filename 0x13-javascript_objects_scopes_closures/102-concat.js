#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  process.exit(1);
}

const [, , file1, file2, destination] = process.argv;

fs.readFile(file1, 'utf8', (err1, data1) => {
  if (err1) {
    process.exit(1);
  }

  fs.readFile(file2, 'utf8', (err2, data2) => {
    if (err2) {
      process.exit(1);
    }

    const concatenatedContent = data1 + data2;

    fs.writeFile(destination, concatenatedContent, 'utf8', (err3) => {
      if (err3) {
        process.exit(1);
      }

      console.log(destination});
    });
  });
});
