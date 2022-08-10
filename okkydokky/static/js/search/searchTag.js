// 태그 검색

function searchTag(params) {
  $("#content_table").on("click", ".btn-info", function () {
    searchTag = $(this).val();
    params["searchKeyword"] = searchTag;

    params["page"] = 1;
    params["startRange"] = 1;

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params);
    } else {
      ajaxMyPageCommon(params);
    }
  });
}
