var DtoSender = function() {
    var CobolTextarea = $("#cobol_textarea");
    var JavaTextarea = $("#java_textarea");

    var dtoSender = {
        clearCobol: function() { CobolTextarea.val(""); },
        submitCobol: function() {
            if (!$.isNumeric($("#number").val())) {
                console.error("PIC is not a valid number");
                return;
            }
            
            $.post({
                url: "/dto_gen",
                data: $("#cobol-form").serialize(),
                success: function(res) { CobolTextarea.val(CobolTextarea.val() + res); }
            });
        },
        submitJava: function() {
            $.post({
                url: "/dto_java",
                data: $("#java-form").serialize(),
                success: function(res) { JavaTextarea.val(res); }
            });
        }
    };

    return dtoSender;
}();