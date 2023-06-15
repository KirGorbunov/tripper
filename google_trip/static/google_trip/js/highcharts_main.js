let xhr = new XMLHttpRequest();

xhr.open('GET', 'http://127.0.0.1:8001/api/v1/tourist-attractions/?limit=1000', false);

try {
  xhr.send();
  if (xhr.status != 200) {
    alert(`Ошибка ${xhr.status}: ${xhr.statusText}`);
  } else {
    var jsonData = JSON.parse(xhr.response);
  }
} catch(err) {
  alert("Запрос не удался");
}

document.addEventListener('DOMContentLoaded', () => {

    Highcharts.chart('container', {
        chart: {
            type: 'scatter',
            zoomType: 'xy',
            width: '1440',
            height: '600',
        },
        xAxis: {
            title: {
                text: 'Rating'
            },
            min: 4
        },

        yAxis: {
            title: {
                text: 'Number of review'
            }
        },

        title: {
            text: 'Popularity and rating of tourist attractions'
        },

        tooltip: {
            headerFormat: '',
            pointFormat: '<a href="{point.url}"><span style="color:{point.color}">{point.name}<br/>Rating: {point.x}<br/>Reports: {point.y}</span><br/></a>'
        },

        plotOptions: {
            series: {
                pointStart: 4
            },
            scatter: {
                point: {
                    events: {
                        click: function () {
                            window.open('../tourist-attractions/'+this.id);
                        }
                    }
                }
            }
        },

        series: [
            {
                name: 'tourist attractions',
                marker: {
                    symbol: 'circle',
                    radius: 3,
                },
                data: jsonData.results,
            }
        ]
    });
});