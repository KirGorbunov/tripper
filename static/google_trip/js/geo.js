window.addEventListener("load", function () {
    const country = document.querySelector('.address-show .country-name');
    const state = document.querySelector('.address-show .state-name');
    const region = document.querySelector('.address-show .region-name');
    const county = document.querySelector('.address-show .county-name');
    const city = document.querySelector('.address-show .city-name');
    const town = document.querySelector('.address-show .town-name');
    const village = document.querySelector('.address-show .village-name');
    const nameTouristAttractions = document.querySelectorAll('.tourist-attractions .name a');
    const nameHotels = document.querySelectorAll('.hotels .name a');
    const nameRestaurants = document.querySelectorAll('.restaurants .name a');
    const photoTouristAttractions = document.querySelectorAll('.tourist-attractions .photo img');
    const photoHotels = document.querySelectorAll('.hotels .photo img');
    const photoRestaurants = document.querySelectorAll('.restaurants .photo img');
    const numberOfReviewTouristAttractions = document.querySelectorAll('.tourist-attractions .number_of_review');
    const numberOfReviewHotels = document.querySelectorAll('.hotels .number_of_review');
    const numberOfReviewRestaurants = document.querySelectorAll('.restaurants .number_of_review');
    const ratingTouristAttractions = document.querySelectorAll('.tourist-attractions .rating__value');
    const ratingHotels = document.querySelectorAll('.hotels .rating__value');
    const ratingRestaurants = document.querySelectorAll('.restaurants .rating__value');
    const linksTouristAttractions = document.querySelectorAll('.tourist-attractions a');
    const linksHotels = document.querySelectorAll('.hotels a');
    const linksRestaurants = document.querySelectorAll('.restaurants a');
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const currentPath = window.location.pathname;
    const countryName = urlParams.get('country__name');
    const stateName = urlParams.get('state__name');
    const regionName = urlParams.get('region__name');
    const countyName = urlParams.get('county__name');
    const cityName = urlParams.get('city__name');
    const townName = urlParams.get('town__name');
    const villageName = urlParams.get('village__name');
    let URLTouristAttractions = location.protocol + '//' + location.host + '/api/v1/tourist-attractions/' + queryString + '&limit=3';
    let URLHotels = location.protocol + '//' + location.host + '/api/v1/hotels/' + queryString + '&limit=3';
    let URLRestaurants = location.protocol + '//' + location.host +  '/api/v1/restaurants/' + queryString + '&limit=3';
    let geoHref = currentPath
    if (countryName) {
        country.innerText = countryName;
        geoHref += '?country__name=' + countryName;
        country.href = geoHref;
    }
    ;
    if (stateName) {
        state.innerText = '> ' + stateName;
        geoHref += '&state__name=' + stateName;
        state.href = geoHref;
    }
    ;
    if (regionName) {
        region.innerText = '> ' + regionName;
        geoHref += '&region__name=' + regionName;
        region.href = geoHref;
    }
    ;
    if (countyName) {
        county.innerText = '> ' + countyName;
        geoHref += '&county__name=' + countyName;
        county.href = geoHref;
    }
    ;
    if (cityName) {
        city.innerText = '> ' + cityName;
        geoHref += '&city__name=' + cityName;
        city.href = geoHref;
    }
    ;
    if (townName) {
        town.innerText = '> ' + townName;
        geoHref += '&town__name=' + townName;
        town.href = geoHref;
    }
    ;
    if (villageName) {
        village.innerText = '> ' + villageName;
        geoHref += '&village__name=' + villageName;
        village.href = geoHref;
    }
    ;

    async function sendRequest(URL) {
        const response = await fetch(URL);
        const data = await response.json();
        return data;
    }

    sendRequest(URLTouristAttractions).then(data => {
        for (let i = 0; i < 3; i++) {
            nameTouristAttractions[i].innerText = data.results[i].name;
            photoTouristAttractions[i].src = data.results[i].photo;
            numberOfReviewTouristAttractions[i].innerText = data.results[i].y + ' reviews';
            ratingTouristAttractions[i].innerText = data.results[i].x;
            linksTouristAttractions[i * 2].href = '/tourist-attractions/' + data.results[i].id;
            linksTouristAttractions[i * 2 + 1].href = '/tourist-attractions/' + data.results[i].id;
        }
    });

    sendRequest(URLHotels).then(data => {
        for (let i = 0; i < 3; i++) {
            nameHotels[i].innerText = data.results[i].name;
            photoHotels[i].src = data.results[i].photo;
            numberOfReviewHotels[i].innerText = data.results[i].y + ' reviews';
            ratingHotels[i].innerText = data.results[i].x;
            linksHotels[i * 2].href = '/hotels/' + data.results[i].id;
            linksHotels[i * 2 + 1].href = '/hotels/' + data.results[i].id;
        }
    });

    sendRequest(URLRestaurants).then(data => {
        for (let i = 0; i < 3; i++) {
            nameRestaurants[i].innerText = data.results[i].name;
            photoRestaurants[i].src = data.results[i].photo;
            numberOfReviewRestaurants[i].innerText = data.results[i].y + ' reviews';
            ratingRestaurants[i].innerText = data.results[i].x;
            linksRestaurants[i * 2].href = '/restaurants/' + data.results[i].id;
            linksRestaurants[i * 2 + 1].href = '/restaurants/' + data.results[i].id;
        }
    });

    initRatings("./rating.js");
});