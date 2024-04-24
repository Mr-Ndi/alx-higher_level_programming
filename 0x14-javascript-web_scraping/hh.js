#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const Data = process.argv[3];

if (!filePath) {
  console.error('Please provide a file path as a command line argument');
  process.exit(1);
}

fs.writeFile(filePath, Data, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(Data);
  }
});
