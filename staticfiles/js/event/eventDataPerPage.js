// N개씩 보기

function eventDataPerPage(params) {
  $("#dataPerPage").change(function () {
    limit = $(this).val();

    params["page"] = 1;
    params["startRange"] = 1;
    params["limit"] = limit;

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
  });
}