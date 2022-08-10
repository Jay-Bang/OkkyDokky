function displayPageNum(params) {
  let pageHtml = "";

  // 첫 페이지
  if (params["startRange"] > 1) {
    pageHtml += `<button class='first_Btn' value="${1}">처음</button>`;
  }
  // 이전 페이지
  if (params["startRange"] > 10) {
    pageHtml += `
        <button class='prev_Btn' value="${
          Number(params["startRange"]) - 1
        }">이전</button>`;
  }
  // 숫자 페이지 페이지
  for (let i = params["startRange"]; i <= params["endRange"]; i++) {
    if (params["page"] == i) {
      pageHtml += `
            <button class='on page_Btn' value="${i}">${i}</button>`;
    } else {
      pageHtml += `
            <button class='page_Btn' value="${i}">${i}</button>`;
    }
  }
  // 다음 페이지
  if (params["endRange"] < params["totalPage"]) {
    pageHtml += `
        <button class='next_Btn' value="${Number(params["endRange"]) + 1}">다음</button>`;
  } else if (params["endRange"] > params["totalPage"]) {
    pageHtml += `
        <button class='next_Btn' value="${0}">다음</button>`;
  }
  // 마지막 페이지
  if (params["page"] < params["totalPage"]) {
    pageHtml += `
        <button class='last_Btn' value="${params["totalPage"]}">마지막</button>`;
  }

  $("#pagination").empty();
  $("#pagination").append(pageHtml);
}