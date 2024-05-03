$(document).ready(function () {
  const event = $('#red_header');
		event.click(function () {
    const head = $(header);
    head.addclass('red');
		});
});
