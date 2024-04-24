#!/usr/bin/node
const fs = require('request');

const url = process.argv[2];

fs.get(ulr, (irabu, response) => {
  if (irabu) {
    console.log(irabu);
  } else {
    answer = response.statusCode;
    console.log(`code: ${answer}`);
  }
});
