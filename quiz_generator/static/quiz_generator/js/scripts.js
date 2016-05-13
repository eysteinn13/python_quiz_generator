/**
 * Created by eysteinn on 12/05/16.
 */

function hide_answers() {
    $(".answer").addClass("hide");
    $(".answer").removeClass("show");
    $(".line").addClass("show");
    $(".line").removeClass("hide");
}

function show_answers() {
    $(".answer").removeClass("hide");
    $(".answer").addClass("show");
    $(".line").addClass("hide");
    $(".line").removeClass("show");
}