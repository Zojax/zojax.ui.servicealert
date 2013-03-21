$(document).ready(function() {
    /*var cookie = $.cookie(service_alert);
    if (!cookie) {
        $(".alert").removeClass("sa-closed");
    }*/

    // set classes for widget items
    $('.configlet-widgets-color ul li').each(function() {
        var $id = $(this).children('input').attr('id');
        $(this).addClass($id);
    });

    var closeAlert = function() {
        $(this).parent().parent().addClass("sa-closed");
        $.cookie(service_alert, 'quick');
	    return false;
    }

    $(".alert .message b").click(closeAlert);
});
