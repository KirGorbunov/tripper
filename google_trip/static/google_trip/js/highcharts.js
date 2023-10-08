function getURL() {
    let URL;
    if (window.location.pathname.includes("tourist-attractions")) {
        URL = 'http://127.0.0.1:8001/api/v1/tourist-attractions/';
        }
    else if (window.location.pathname.includes("hotels")) {
        URL = 'http://127.0.0.1:8001/api/v1/hotels/';
    }
    else if (window.location.pathname.includes("restaurants")) {
        URL = 'http://127.0.0.1:8001/api/v1/restaurants/';
    }
    return URL;
}

currentId = parseInt(window.location.pathname.match(/\d+/));
console.log(currentId)

// async function sendRequest(method, url) {
//     const response = await fetch(url);
//     const data = await response.json();
//     console.log(data)
//     return data
// }
//
//
// sendRequest('GET', getURL()).then(jsonData => {
//     jsonData;
// })

let xhr = new XMLHttpRequest();

xhr.open('GET', getURL(), false);

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

let result = jsonData.filter((item) => item.id === currentId);
let currentData = result[0];

console.log(currentData.x)
console.log(currentData.y)

jsonData = jsonData.filter((item) => item.id != currentId & item.country_id === currentData.country_id);

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
            min: Math.min(currentData.x, 4)
        },

        yAxis: {
            title: {
                text: 'Number of review'
            }
        },

        title: {
            text: 'Popularity and rating'
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<a href="{point.url}"><span style="color:{point.color}">{point.name}<br/>Rating: {point.x}<br/>Reports: {point.y}</span><br/></a>'
        },

        plotOptions: {
            series: {
                pointStart: Math.min(currentData.x, 4)
            },
            scatter: {
                point: {
                    events: {
                        click: function () {
                            window.open('../'+this.id);
                        }
                    }
                }
            }
        },

        series: [
            {
                name: 'Selected object',
                marker: {
                    symbol: 'triangle'
                },
                data: [currentData],
                color: 'red',
            },
            {
                name: 'Other objects',
                marker: {
                    symbol: 'circle'
                },
                data: jsonData,
                turboThreshold: 10000,
            },
        ]
    });
});