const CobolTextarea = $("#cobol_textarea");
const JavaTextarea = $("#java_textarea");

const DtoSender = {
    clearCobol: () => { CobolTextarea.val(""); },
    submitCobol: () => {
        if (!$.isNumeric($("#number").val())) {
            console.error("PIC is not a valid number");
            return;
        }
        
        $.post({
            url: "/dto_gen",
            data: $("#cobol-form").serialize(),
            success: (res) => { CobolTextarea.val(CobolTextarea.val() + res); }
        });
    },
    submitJava: () => {
        $.post({
            url: "/dto_java",
            data: $("#java-form").serialize(),
            success: (res) => { JavaTextarea.val(JavaTextarea.val() + res); }
        });
    }
};

export default DtoSender;