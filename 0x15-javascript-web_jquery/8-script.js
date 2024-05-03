$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    datatype: 'json',
    success: function (data) {
      const mtitle = '';
      $.each(data.results, function (index, value) {
        mtitle += '<li>' + value.title + '</li>';
      });
      $('UL#list_movies').html(mtitle);
    }
  });
});
