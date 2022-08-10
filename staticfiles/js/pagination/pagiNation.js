// 처음 페이지 이벤트

function pagiNation(params) {
  // 첫 페이지
  $("#pagination").on("click", ".first_Btn", function () {
    page = $(this).val();

    params["page"] = Number(page);
    params["startRange"] = Number(page);
    params["endRange"] = Number(page) + 9;

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
  });
  // 이전 페이지
  $("#pagination").on("click", ".prev_Btn", function () {
    page = $(this).val();

    params["page"] = Number(page);
    params["startRange"] = Number(page) - 9;
    params["endRange"] = Number(page);

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
  });
  // 번호 페이지
  $("#pagination").on("click", ".page_Btn", function () {
    page = $(this).val();

    params["page"] = Number(page);

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
  });
  // 다음 페이지
  $("#pagination").on("click", ".next_Btn", function () {
    page = $(this).val();

    params["page"] = Number(page);
    params["startRange"] = Number(page);
    params["endRange"] = Number(page) + 9;
    params["prevEndRange"] = Number(page) - 1;

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
  });
  // 마지막 페이지
  $("#pagination").on("click", ".last_Btn", function () {
    page = $(this).val();

    params["page"] = Math.ceil(Number(page));
    params["startRange"] = Math.floor((Number(page) - 1) / 10) * 10 + 1;
    params["endRange"] = Math.ceil(Number(page));
    params["prevEndRange"] = Math.floor(Number(page) / 10) * 10;

    // console.log("here1:", params["endRange"], params["totalPage"]);

    if (params["url"] == "/okkydokky/board/") {
      ajaxBoardCommon(params)
    } else {
      ajaxMyPageCommon(params)
    }
    // console.log("here2:", params["endRange"], params["totalPage"]);
  });
}
