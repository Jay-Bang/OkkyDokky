// Scrap Alert Messege

function ajaxScrapMsg(tr_id) {
  $.ajax({
    url: "../../okkydokky/scrap/" + tr_id + "/",
    method: "GET",
    dataType: "json",
    data: '',
    success: function (result) {
      alert(result["message"]);
    },
  });
}