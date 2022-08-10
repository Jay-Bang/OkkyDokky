function ajaxBoard(params) {
  $.ajax({
    url: params["url"],
    method: "GET",
    dataType: "json",
    data: params,
    success: function (result) {
      resultSet = result;
      console.log(result)
      qslist = resultSet["qslist"];

      params["totalData"] = resultSet["totalData"];
      params["totalPage"] = resultSet["totalPage"];
      params["startRange"] = resultSet["startRange"];
      params["endRange"] = resultSet["endRange"];
      params["nextStartRange"] = resultSet["nextStartRange"];

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
