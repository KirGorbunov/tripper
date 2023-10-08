const latitude = document.querySelector('.latitude').innerHTML
const longitude = document.querySelector('.longitude').innerHTML
const name = document.querySelector('.name').innerHTML
console.log(latitude)
console.log(longitude)
console.log(name)
ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
    center: [latitude, longitude],
    zoom: 13
    });
    myMap.setType('yandex#hybrid');
    var placemark = new ymaps.Placemark([latitude, longitude]);
    placemark.name = name;
    myMap.geoObjects.add(placemark);
}