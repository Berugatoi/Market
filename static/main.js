let path = location.protocol + '//' + location.host;
path += '/';
alert(document.cookie)

let Switch = function (prod_id) {
    let all_img = document.getElementsByClassName('favorite_icon')
    let current = all_img.namedItem(prod_id);
    if (current.src == path + 'static/icons/empty_heart.jpg') {
        current.src = 'static/icons/full_heart.jpg';
        let key_vals = document.cookie.split('; ')
        for (let i = 0; i < key_vals.length; i++){
            let val = key_vals[i].split('=');
            if ('UserCookie' == val[0]) {
              let products = val[1];
              products += ';'
              products += 4;
              return;
            }
}
        document.cookie = 'UserCookie=' + prod_id
    }
    else {
        current.src = 'static/icons/empty_heart.jpg';
    }

}