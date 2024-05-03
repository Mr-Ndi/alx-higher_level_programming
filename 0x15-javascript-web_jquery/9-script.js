$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    dataType: 'json',
    success: function (data) {
      const hello = data.hello;
      $('#hello').text(hello);
    }
  });
});
