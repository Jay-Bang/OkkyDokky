function displayChart(params) {
  const el = document.getElementById("chart-area 1");
  const data = {
    categories: ["Data"],
    series: [
      {
        name: "채택 답변이 있는 게시글",
        data: params["checkedAnswer"],
      },
      {
        name: "답변만 있는 게시글",
        data: params["unCheckedAnswer"],
      },
      {
        name: "답변 없는 게시글",
        data: params["noAnswer"],
      },
    ],
  };

  const options = {
    chart: { title: "Your Data Status", width: 600, height: 500 },
    series: {
      dataLabels: {
        visible: true,
        pieSeriesName: {
          visible: true,
          anchor: "outer",
        },
      },
    },
    reseponsive: { animation: false },
    legend: { align: "bottom", selectable: false },
  };

  const chart = toastui.Chart.pieChart({ el, data, options });
}
