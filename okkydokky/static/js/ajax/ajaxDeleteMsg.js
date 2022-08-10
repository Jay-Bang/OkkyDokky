// Delete Alert Messege

function ajaxDeleteMsg(tr_id) {
  $.ajax({
    url: "../../../okkydokky/delete/" + tr_id + "/",
    method: "GET",
    dataType: "json",
    data: '',
    success: function (result) {
      alert(result["message"]);
    },
  });
}