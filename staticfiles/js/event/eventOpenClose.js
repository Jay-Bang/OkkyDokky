// 답변내용 보기/닫기

function eventOpenClose() {
  $("#content_table").on("click", ".comment_btn", function () {
    let tr_id = this.id;
    tr_id = tr_id.split("_")[1];
    tr_id = "tr_comment_" + tr_id;
    let value = $("#" + this.id).val();

    if (value == "open") {
      $("#" + tr_id).show();
      $("#" + this.id).val("close");
      $("#" + this.id).text("내용닫기");
    } else if ((value = "close")) {
      $("#" + tr_id).hide();
      $("#" + this.id).val("open");
      $("#" + this.id).text("내용보기");
    }
  });
}