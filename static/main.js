let path = location.protocol + '//' + location.host + '/';


let Switch = function (prod_id) {
//    Получаю <img> по классу и id
    let all_img = document.getElementsByClassName('favorite_icon')
    let current = all_img.namedItem(prod_id);
// Проверяю пустое ли сердечко
    if (current.src == path + 'static/icons/empty_heart.jpg') {
        current.src = 'static/icons/full_heart.jpg';
        let cookies = convertStringToObject(document.cookie);
            if (cookies['UserCookie']){
                console.log(String(prod_id));
                console.log(cookies[' UserCookie'].split(':'));
                console.log((String(prod_id) in cookies['UserCookie'].split(':')));
                if (!cookies['UserCookie'].includes(String(prod_id))) {
                    let new_val = 'UserCookie=' + cookies['UserCookie'] + ':' + String(prod_id);
                    document.cookie = new_val;
             }

        }
        else {
            document.cookie = 'UserCookie=' + String(prod_id);


        }}
    else {
        current.src = 'static/icons/empty_heart.jpg';
    }

}


let addToCart = function(prod_id){
    let cookies = convertStringToObject(document.cookie);
    if (cookies['Cart']){
        if (!cookies['Cart'].includes(String(prod_id))) {
            let new_val = 'Cart=' + cookies['Cart'] + ':' + String(prod_id);
            document.cookie = new_val;
     }
}
    else {
        document.cookie = 'Cart=' + String(prod_id)
    }
}


var convertStringToObject = function(s){
    let res = {},
    tmp = '';

    var a = s.split('; ');
    a.forEach(function(item, i, arr){
        let v = item.split('=');
        res[v[0]] = v[1];
    });

    return res;
}
