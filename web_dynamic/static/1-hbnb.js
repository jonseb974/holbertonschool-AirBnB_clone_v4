const $ = window.$;

$('document').ready(function () {
  const amenities = {}; // create an empty list
  $('input[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) { // if their is a check
      amenities[$(this).attr('data-id')] = $(this).attr('data-name'); // corresponding name is set to the id.
    } else {
      delete amenities[$(this).attr('data-id')]; // if box is uncheck remove data.
    }
    $('.amenities H4').text(Object.values(amenities).join(', '));
  });
});
