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
    const ratingTouristAttractions = document.querySelectorAll('.tourist-attractions .rating');
    const ratingHotels = document.querySelectorAll('.hotels .rating');
    const ratingRestaurants = document.querySelectorAll('.restaurants .rating');


    console.log(photoTouristAttractions)

    countriesForChoice.forEach(el => {
        el.addEventListener('click', () => {
            let CountryName = el.innerText;
            console.log(CountryName);
            country.innerText = CountryName;
            let URLTouristAttractions = 'http://127.0.0.1:8001/api/v1/tourist-attractions/?country__name=' + CountryName + '&limit=3';
            let URLHotels = 'http://127.0.0.1:8001/api/v1/hotels/?country__name=' + CountryName+'&limit=3';
            let URLRestaurants = 'http://127.0.0.1:8001/api/v1/restaurants/?country__name=' + CountryName+'&limit=3';

            function xhrConnect(method, URL, async = false) {
                let xhr = new XMLHttpRequest();
                xhr.open(method, URL, async);
                try {
                    xhr.send();
                    if (xhr.status != 200) {
                        alert(`Ошибка ${xhr.status}: ${xhr.statusText}`);
                    } else {
                        var jsonData = JSON.parse(xhr.response);
                        console.log(jsonData);
                        return jsonData;
                    }
                } catch (err) { // для отлова ошибок используем конструкцию try...catch вместо onerror
                    alert("Запрос не удался");
                }
            }

            let TouristAttractionsJSON = xhrConnect('GET', URLTouristAttractions, false);
            let HotelsJSON = xhrConnect('GET', URLHotels, false);
            let RestaurantsJSON = xhrConnect('GET', URLRestaurants, false);
            console.log(TouristAttractionsJSON);

            for (let i = 0; i < 3; i++) {
                nameTouristAttractions[i].innerText = TouristAttractionsJSON.results[i].name;
                nameTouristAttractions[i].href = '/tourist-attractions/'+TouristAttractionsJSON.results[i].id;
                nameHotels[i].innerText = HotelsJSON.results[i].name;
                nameHotels[i].href = '/hotels/'+HotelsJSON.results[i].id;
                nameRestaurants[i].innerText = RestaurantsJSON.results[i].name;
                nameRestaurants[i].href = '/restaurants/'+RestaurantsJSON.results[i].id;
                photoTouristAttractions[i].src = TouristAttractionsJSON.results[i].photo;
                photoHotels[i].src = HotelsJSON.results[i].photo;
                photoRestaurants[i].src = RestaurantsJSON.results[i].photo;
                numberOfReviewTouristAttractions[i].innerText = TouristAttractionsJSON.results[i].y;
                numberOfReviewHotels[i].innerText = HotelsJSON.results[i].y;
                numberOfReviewRestaurants[i].innerText = RestaurantsJSON.results[i].y;
                ratingTouristAttractions[i].innerText = TouristAttractionsJSON.results[i].x;
                ratingHotels[i].innerText = HotelsJSON.results[i].x;
                ratingRestaurants[i].innerText = RestaurantsJSON.results[i].x;
            }
        });
    });
})