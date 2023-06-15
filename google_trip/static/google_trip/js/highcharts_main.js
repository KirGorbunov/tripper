document.addEventListener('DOMContentLoaded', () => {
    constructChart('tourist-attractions');
});


function constructChart(type) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8001/api/v1/' + type + '/?limit=1000', false);

    try {
        xhr.send();
        if (xhr.status != 200) {
            alert(`Ошибка ${xhr.status}: ${xhr.statusText}`);
        } else {
            var jsonData = JSON.parse(xhr.response);
        }
    } catch (err) {
        alert("Запрос не удался");
    }

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
            text: 'Popularity and rating of ' + type
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
                            window.open('../'+ type + '/' + this.id);
                        }
                    }
                }
            }
        },

        series: [
            {
                name: type,
                marker: {
                    symbol: 'circle',
                    radius: 3,
                },
                data: jsonData.results,
            }
        ]
    })
}


window.addEventListener("load", function () {
    const tourist_attraction_button = document.querySelector('.index_img.tourist_attractions_index_image');
    const hotels_button = document.querySelector('.index_img.hotels_index_image');
    const restaurants_attraction_button = document.querySelector('.index_img.restaurants_index_image');

    tourist_attraction_button.addEventListener('click', () => {
        constructChart('tourist-attractions');
    });
    hotels_button.addEventListener('click', () => {
        constructChart('hotels');
    });
    restaurants_attraction_button.addEventListener('click', () => {
        constructChart('restaurants');
    });
});




