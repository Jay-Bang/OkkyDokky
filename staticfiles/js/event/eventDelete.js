// 삭제

function eventDelete() {
  $("#content_table").on("click", ".delete_btn", function () {
    console.log("clicked");
    let tr_id = this.id;
    tr_id = tr_id.split("_")[1];

    ajaxDeleteMsg(tr_id)
  });
}