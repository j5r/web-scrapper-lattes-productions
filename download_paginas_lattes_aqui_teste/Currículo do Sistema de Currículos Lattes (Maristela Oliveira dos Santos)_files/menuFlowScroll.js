/*topo */
$(document).ready(function () {
    var el = $('.menu-header');
    var elpos_original = el.offset().top;
    el.css({
        'position': 'absolute',
        'top': '15px'
    });
    el.fadeIn("slow")
    $(window).scroll(function () {
        var elpos = el.offset().top;
        var windowpos = $(window).scrollTop();
        var finaldestination = windowpos;
        if (windowpos < 148) {
            finaldestination = elpos_original;
            el.stop().css({
                'top': 15
            });
            $(".menuScroll .tituloFlow").html("")
            el.removeClass("menuScroll");
        } else {
            el.stop().animate({
                'top': finaldestination - elpos_original + 15
            }, 0);
            el.addClass("menuScroll");
        }
    });
});
/*Titulos*/
$(window).scroll(function () {
    $(".title-wrapper").each(function () {
        textFlow = ""
        var windFlow = $(window).scrollTop();
        var topFlow = $(this).find("h1").offset().top
        if (topFlow < windFlow + 20) {
            textFlow = $(this).find("h1").html()
            $(".menuScroll .tituloFlow").html(textFlow)
        }
    });
});
/*rodape */
$(function () {
    $.fn.scrollToTop = function () {
        $(this).hide().removeAttr("href");
        if ($(window).scrollTop() != "0") {
            $(this).fadeIn("slow")
        }
        var scrollDiv = $(this);
        $(window).scroll(function () {
            if ($(window).scrollTop() < "500") {
                $(scrollDiv).fadeOut("slow")
            } else {
                $(scrollDiv).fadeIn("slow")
            }
        });
        $(this).click(function () {
            $("html, body").animate({
                scrollTop: 0
            }, "slow")
        })
    }
});
$(function () {
    $("#toTop").scrollToTop();
});