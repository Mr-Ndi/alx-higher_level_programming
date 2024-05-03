$(document).ready(function () {
  const event = $('#red_header');
		event.click(function () {
    const head = $('header');
    head.css('color', '#FF0000');
		});
});
