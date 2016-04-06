!function ($) {

    var defaults = {
        entrance: "bottom",
        column: 4,
        margin: "1%",
        selector: "> li",
        hoverTilt: "right",
    };


    $.fn.tip_cards = function (options) {
        var settings = $.extend({}, defaults, options),
            el = $(this);
        el.addClass("tc_body");

        $.each(el.find(settings.selector), function (i) {
            $(this).addClass("tc_card").hide().css({
                "width": (100 / settings.column) - (parseInt(settings.margin) * 2) + "%",
                "margin": settings.margin
            }).wrapInner("<div class='tc_inner_card tilt_" + settings.hoverTilt + "'></div>");
            if ($(this).find(".tc_front").length > 0) {
                $(this).find(".tc_inner_card").addClass("tc_flipped");
            }
        });


        setTimeout(function () {
            $.each(el.find(".tc_card"), function (i) {
                var current = $(this);
                current.addClass("animate tc_entrance_" + settings.entrance).show();
                current.find(".tc_inner_card").prepend("<span class='tc_shadow'></span>");

                if (current.find(".tc_front").length > 0) {
                    setTimeout(function () {
                        current.find(".tc_inner_card").removeClass("tc_flipped")
                    }, 600);
                }
            });
        }, 100);


    }
}(window.jQuery);

