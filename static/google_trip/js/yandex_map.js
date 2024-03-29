const latitude = document.querySelector('.latitude').innerHTML
const longitude = document.querySelector('.longitude').innerHTML
const name = document.querySelector('#object_name').innerHTML
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