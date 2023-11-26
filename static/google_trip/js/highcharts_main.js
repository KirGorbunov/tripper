window.addEventListener("load", function () {
    const countriesForChoice = document.querySelectorAll('.country-navigation ul li');
    countriesForChoice.forEach(el => {
        el.addEventListener('click', () => {
            let CountryName = el.innerText;
            let CounterQuery = 'country__name=' + CountryName
            let activeType = document.querySelector('.places .active span').innerText.toLowerCase().replace(" ", "-");
            constructChart(activeType, CounterQuery);
        });
    });
});

window.addEventListener("load", function () {
    const tourist_attraction_button = document.querySelector('.index_img.tourist_attractions_index_image');
    const hotels_button = document.querySelector('.index_img.hotels_index_image');
    const restaurants_attraction_button = document.querySelector('.index_img.restaurants_index_image');

    tourist_attraction_button.addEventListener('click', () => {
        let countryNameObj = document.querySelector('.country-name h2');
        if (countryNameObj) {
            let countryName = countryNameObj.innerText
            if (countryName == 'World') {
                let CounterQuery = ''
                constructChart('tourist-attractions', CounterQuery);
            } else {
                let CounterQuery = 'country__name=' + countryName
                constructChart('tourist-attractions', CounterQuery);
            }
        }
        else {
            constructChart('tourist-attractions', '');
        }
        tourist_attraction_button.classList.add('active');
        hotels_button.classList.remove('active');
        restaurants_attraction_button.classList.remove('active');
    });

    hotels_button.addEventListener('click', () => {
        let countryNameObj = document.querySelector('.country-name h2');
        if (countryNameObj) {
            let countryName = countryNameObj.innerText
            if (countryName == 'World') {
                let CounterQuery = ''
                constructChart('hotels', CounterQuery);
            } else {
                let CounterQuery = 'country__name=' + countryName
                constructChart('hotels', CounterQuery);
            }
        }
        else {
            constructChart('hotels', '');
        }
        tourist_attraction_button.classList.remove('active');
        hotels_button.classList.add('active');
        restaurants_attraction_button.classList.remove('active');
    });

    restaurants_attraction_button.addEventListener('click', () => {
        let countryNameObj = document.querySelector('.country-name h2');
        if (countryNameObj) {
            let countryName = countryNameObj.innerText
            if (countryName == 'World') {
                let CounterQuery = ''
                constructChart('restaurants', CounterQuery);
            } else {
                let CounterQuery = 'country__name=' + countryName
                constructChart('restaurants', CounterQuery);
            }
        }
        else {
            constructChart('restaurants', '');
        }
        tourist_attraction_button.classList.remove('active');
        hotels_button.classList.remove('active');
        restaurants_attraction_button.classList.add('active');
    });
});

async function sendRequest(type, CounterQuery) {
    const queryString = window.location.search;
    let URL = location.protocol + '//' + location.host + '/api/v1/' + type + '/?' + CounterQuery + '&rating__gte=4.0&limit=1000&' + queryString.slice(1);
    const response = await fetch(URL);
    const data = await response.json();
    return data;
}

function constructChart(type, CounterQuery) {
    sendRequest(type, CounterQuery).then(data => {
        let used = [];
        let newData = [];
        let activeType = document.querySelector('.places .active span').innerText.toLowerCase().replace(" ", "-");
        for (let i = 0; i < data.results.length; i++) {
            let countryCurrentId = data.results[i].country_name
            if (!used.includes(countryCurrentId)) {
                used.push(countryCurrentId);
                let obj_data = data.results.filter((item) => item.country_name === countryCurrentId);
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
                // width: '1440',
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
                text: 'Popularity and rating'
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
                                window.open('../' + activeType + '/' + this.id);
                            }
                        }
                    }
                }
            },
            series: newData,
        })
    })
}

document.addEventListener('DOMContentLoaded', () => {
    constructChart('tourist-attractions', '');
});