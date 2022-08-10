// 스크랩

function eventScrap() {
  $("#content_table").on("click", ".scrap_btn", function () {
    console.log("clicked");
    let tr_id = this.id;
    tr_id = tr_id.split("_")[1];

    ajaxScrapMsg(tr_id)
  });
}