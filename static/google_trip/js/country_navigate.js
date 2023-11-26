document.querySelector('#search').oninput = function () {
    let val = this.value.trim().toLowerCase();
    let countries = document.querySelectorAll('.search li');
    if (val != '') {
        countries.forEach(function (elem) {
            if (elem.innerText.toLowerCase().search(val) == -1) {
                elem.classList.add('hide');
                elem.innerHTML = elem.innerText;
            }
            else {
                elem.classList.remove('hide');
                let searchStr = elem.innerText;
                elem.innerHTML = insertMark(searchStr, elem.innerText.toLowerCase().search(val), val.length)
            }
        });
    }
    else {
        countries.forEach(function (elem) {
            elem.classList.remove('hide');
            elem.innerHTML = elem.innerText;
        })
    }
}

function insertMark(countryName, pos, len) {
    return countryName.slice(0, pos) + '<mark>' + countryName.slice(pos, pos+len) + '</mark>' + countryName.slice(pos+len);
}