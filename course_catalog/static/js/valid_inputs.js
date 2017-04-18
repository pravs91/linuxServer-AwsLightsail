// disable submit button if input is empty using jquery
// go to prev page on clicking cancel
$(function(){
    $('#submit-button').attr('disabled', 'disabled');
    // use this to detect pre-filled values in edit
    $('.form-group > input').each(function() {
        if ($(this).val() != '' || ($('#description')[0].value != "")) {
            $('#submit-button').removeAttr('disabled');
        }
    });

    // disable submit button if any input is empty
    $('.form-group > input, textarea').keyup(function() {

        var empty = false;
        $('.form-group > input').each(function() {
            if ($(this).val() == '' || ($('#description')[0].value == "")) {
                empty = true;
            }
        });
        if (empty) {
            $('#submit-button').attr('disabled', 'disabled'); 
        } else {
            $('#submit-button').removeAttr('disabled'); 
        }
    });
    $('#cancel-button').on('click',function(){
        window.location.href = window.history.back();
    })
});
