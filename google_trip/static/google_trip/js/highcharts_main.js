document.addEventListener('DOMContentLoaded', () => {
    constructChart('tourist-attractions');
});


function constructChart(type) {
    const queryString = window.location.search;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8001/api/v1/' + type + '/?rating__gte=4.0&limit=1000&' + queryString.slice(1), false);

    try {type
        xhr.send();
        if (xhr.status != 200) {
            alert(`Ошибка ${xhr.status}: ${xhr.statusText}`);
        } else {
            var jsonData = JSON.parse(xhr.response);
        }
    } catch (err) {
        alert("Запрос не удался");
    }

    let used = [];
    let newData = [];
    console.log(jsonData.results.length)


    for (let i = 0; i < jsonData.results.length; i++) {
        let countryCurrentId = jsonData.results[i].country_name
        if (!used.includes(countryCurrentId)) {
            used.push(countryCurrentId);
            let obj_data = jsonData.results.filter((item) => item.country_name === countryCurrentId);
            let obj = {
                name: countryCurrentId,
                data: obj_data
            };
            newData.push(obj);
        };
    };

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
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
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

        series: newData
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




