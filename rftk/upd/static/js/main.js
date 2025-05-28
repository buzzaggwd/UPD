$('#add-section-btn').click(function() {
    $('#section-modal').modal('show');
});

$('#section-form').submit(function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/add_section/',
        data: $(this).serialize(),
        success: function(response) {
            $('#product-section').append(`<option value="${response.id}">${response.name}</option>`);
            $('#section-modal').modal('hide');
        }
    });
});