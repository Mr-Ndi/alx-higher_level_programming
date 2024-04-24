#!/usr/bin/node
const request = require('request');

const id = 18;

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request.get(url, (irabu, response, body) => {
  if (irabu) {
    console.log(irabu);
  } else {
    const num = (JSON.parse(body)).length;
    console.log(num);
  }
});
