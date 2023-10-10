const countryName = document.querySelector('#country_name').innerHTML
function getURL(countryName) {
    let URL;
    if (window.location.pathname.includes("tourist-attractions")) {
        URL = 'http://127.0.0.1:8001/api/v1/tourist-attractions/';
    } else if (window.location.pathname.includes("hotels")) {
        URL = 'http://127.0.0.1:8001/api/v1/hotels/';
    } else if (window.location.pathname.includes("restaurants")) {
        URL = 'http://127.0.0.1:8001/api/v1/restaurants/';
    }
    return URL + '?country__name=' + countryName;
}

currentId = parseInt(window.location.pathname.match(/\d+/));
console.log(currentId)

let URL = getURL(countryName)
console.log(URL)

async function sendRequest(URL) {
    const response = await fetch(URL);
    const data = await response.json();
    return data
}

sendRequest(URL).then((data) => {
    let result = data.filter((item) => item.id === currentId);
    let currentData = result[0];

    jsonData = data.filter((item) => item.id != currentId);

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
                            window.open('../' + this.id);
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