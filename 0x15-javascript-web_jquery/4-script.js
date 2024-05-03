$(document).ready(function () {
  $('#toggle_header').on('click', function () {
    const currentClass = $('header').attr('class');
    if (currentClass === 'red') {
      $('header').removeClass('red').addClass('green');
    } else if (currentClass === 'green') {
      $('header').removeClass('green').addClass('red');
    }
  });
});
