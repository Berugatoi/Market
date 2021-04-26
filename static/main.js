let path = location.protocol + '//' + location.host;
path += '/';

let Switch = function (prod_id) {
    let all_img = document.getElementsByClassName('favorite_icon')
    let current = all_img.namedItem(prod_id);
    if (current.src == path + 'static/icons/empty_heart.jpg') {
        current.src = 'static/icons/full_heart.jpg';
    }
    else {
        current.src = 'static/icons/empty_heart.jpg';
    }
}