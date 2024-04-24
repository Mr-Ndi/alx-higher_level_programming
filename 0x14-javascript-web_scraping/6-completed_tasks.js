#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
const dict = {};

request(link, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dict)) {
          dict[userid] = 0;
        }
        dict[userid] += 1;
      }
    });
    console.log(dict);
  }
});
