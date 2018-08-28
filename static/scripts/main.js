$(function() {
    $("body")
        .on("click", "#clear_cobol", DtoSender.clearCobol)
        .on("click", "#submit_cobol", DtoSender.submitCobol)
        .on("click", "#submit_java", DtoSender.submitJava);
});