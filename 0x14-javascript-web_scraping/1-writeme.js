#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const Data = process.argv[3];

if (!filePath) {
  console.error('Please provide a file path as a command line argument');
  process.exit(1);
}

fs.writeFile(filePath, { encoding: 'utf-8' }, Data, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(Data);
  }
});
