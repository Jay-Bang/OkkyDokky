function displayTable(qslist) {
  let tableHtml;

  for (i = 0; i < qslist.length; i++) {
    htmlString1 = "";
    htmlString2 = "";
    htmlString3 = "";
    if (qslist[i][8] == "") {
      htmlString1 += `${qslist[i][2]}`;
    } else if (qslist[i][8]) {
      htmlString1 += `<mark><b>${qslist[i][2]}<b></mark>`;
    }
    if (qslist[i][7] == "") {
      tableHtml += `pass`;
    } else if (qslist[i][7]) {
      for (j = 0; j < qslist[i][7].length; j++) {
        htmlString2 += `<button class="btn btn-info btn-sm" value="${qslist[i][7][j]}">
                    ${qslist[i][7][j]}</button>`;
      }
    }
    for (k = 0; k < qslist[i][6].length; k++) {
      htmlString3 += `<a class="badge badge-secondary">
                    ${qslist[i][6][k]}</a>`;
    }

    tableHtml += `
            <tr id="tr_${qslist[i][0]}">
                <td style="text-align:center">${qslist[i][10]}</td>
                <td>${htmlString1} ${htmlString3}<br>
                    ${htmlString2}<br>
                </td>
                <td style="text-align:center"><a href=${qslist[i][1]}>${qslist[i][1]}</a></td>
                <td style="text-align:center">${qslist[i][3]}</td>
                <td style="text-align:center">${qslist[i][4]}</td>
                <td style="text-align:center">
                    <button id="btn_${qslist[i][0]}" class="comment_btn" value="open">내용보기</button>
                </td>
                <td style="text-align:center">
                    <button id="btn_${qslist[i][0]}" class="scrap_btn" value="get">담기</button>
                </td>
            <tr>
            <tr id="tr_comment_${qslist[i][0]}" class="tr_comment">
                <td></td>
                <td colspan="1">
                    <h2><mark><b>질문<b></mark></h2><br><br><br>
                    ${qslist[i][5]}
                </td>
                <td colspan="2">
                    <h2><mark><b>채택답변<b></mark></h2><br><br><br>
                    ${qslist[i][8]}
                </td>
                <td colspan="1" style="text-align:center">
                    ${qslist[i][9]}
                </td>
                <td></td>
                <td></td>
            <tr>`;
  }

  $("#content_table").empty();
  $("#content_table").append(tableHtml);
  $(".tr_comment").hide();
}
