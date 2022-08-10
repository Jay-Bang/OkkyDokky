function ajaxBoardCommon(params) {
  $.ajax({
    url: params["url"],
    method: "GET",
    dataType: "json",
    data: params,
    success: function (result) {
      resultSet = result;
      qslist = resultSet["qslist"];

      params["totalData"] = resultSet["totalData"];
      params["totalPage"] = resultSet["totalPage"];

      if (result["totalPage"] >= 10) {
        params["endRange"] = params["startRange"] + 9;
        if (params["endRange"] > params["totalPage"]) {
          params["endRange"] = params["totalPage"];
        }
      } else if (params["endRange"] > result["totalPage"]) {
        params["endRange"] = result["totalPage"];
      }

      if (params["url"] == "/okkydokky/board/") {
        displayTable(qslist);
      } else {
        displayScrapedTable(qslist);
      }

      displayPageNum(params);

      console.log(params, resultSet);
    },
  });
}
