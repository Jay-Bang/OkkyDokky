// 키워드 검색

function searchKeyword(params) {
  $("#searchBtn").click(function () {
    searchKeyword = $("#searchKeyword").val();
    conditionVal = $("#conditionVal").prop("selected", true).val();

    params["page"] = 1;
    params["startRange"] = 1;
    // params["startRange"] = resultSet["startRange"];
    // params["endRange"] = resultSet["endRange"];
    // params['nextStartRange'] = resultSet['nextStartRange']
    params["searchKeyword"] = searchKeyword;
    params["conditionVal"] = conditionVal;
    params["totalData"] = resultSet["totalData"];
    params["totalPage"] = resultSet["totalPage"];

    if (params["totalPage"] >= 10) {
      params["endRange"] = 10;
    } else {
      params["endRange"] = params["totalPage"];
    }

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
  });
}
