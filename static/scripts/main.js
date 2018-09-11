$(function() {
    $("body")
        .on("click", "#clear_cobol", DtoSender.clearCobol)
        .on("click", "#submit_cobol", DtoSender.submitCobol)
        .on("click", "#submit_java", DtoSender.submitJava)
        .on("keydown", ".send_enter", function(ev) { if (ev.keyCode === 13) DtoSender.submitCobol(); });
});