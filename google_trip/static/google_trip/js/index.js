window.addEventListener("load", function () {
    const country = document.querySelector('.country-name h2');
    const countriesForChoice = document.querySelectorAll('.country-navigation ul li');
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
    const linksAllTouristAttractions = document.querySelector('.tourist-attractions .choose_button');
    const linksAllHotels = document.querySelector('.hotels .choose_button');
    const linksAllRestaurants = document.querySelector('.restaurants .choose_button');

    countriesForChoice.forEach(el => {
        el.addEventListener('click', () => {
            let CountryName = el.innerText;
            country.innerText = CountryName;
            let URLTouristAttractions = location.protocol + '//' + location.host + '/api/v1/tourist-attractions/?country__name=' + CountryName + '&limit=3';
            let URLHotels = location.protocol + '//' + location.host + '/api/v1/hotels/?country__name=' + CountryName + '&limit=3';
            let URLRestaurants = location.protocol + '//' + location.host + '/api/v1/restaurants/?country__name=' + CountryName + '&limit=3';
            linksAllTouristAttractions.href = '/tourist-attractions/?country__name=' + CountryName;
            linksAllHotels.href = '/hotels/?country__name=' + CountryName;
            linksAllRestaurants.href = '/restaurants/?country__name=' + CountryName

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
    });
});