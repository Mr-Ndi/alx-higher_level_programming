$(document).ready(function () {
  const element = $('header');

  if (element) {
    element.css('color', '#FF0000');
  } else {
    console.error('Header element is not found');
  }
});
