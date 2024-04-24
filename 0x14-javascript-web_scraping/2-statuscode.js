#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (irabu, response, body) {
  if (irabu) {
    console.log(irabu);
  } else {
    console.log('code:', response.statusCode);
  }
});
