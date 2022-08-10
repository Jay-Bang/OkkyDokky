function ajaxMyPage(params) {
  $.ajax({
    url: params["url"],
    method: "GET",
    dataType: "json",
    data: params,
    success: function (result) {
      resultSet = result;
      qslist = resultSet["qslist"];

      console.log(result);

      params["totalData"] = resultSet["totalData"];
      params["totalPage"] = resultSet["totalPage"];
      params["startRange"] = resultSet["startRange"];
      params["endRange"] = resultSet["endRange"];
      params["nextStartRange"] = resultSet["nextStartRange"];
      params["myPage"] = resultSet["myPage"];
      params["noAnswer"] = resultSet["noAnswer"];
      params["checkedAnswer"] = resultSet["checkedAnswer"];
      params["unCheckedAnswer"] = resultSet["unCheckedAnswer"];

      if (params["url"] == "/okkydokky/board/") {
        displayTable(qslist);
      } else {
        displayScrapedTable(qslist);
      }

      displayPageNum(params);

      displayChart(params);

      console.log(params);

      return resultSet;
    },
  });
}
