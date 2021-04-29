let path = location.protocol + '//' + location.host + '/';


let Switch = function (prod_id) {
//    Получаю <img> по классу и id
    let all_img = document.getElementsByClassName('favorite_icon')
    let current = all_img.namedItem(prod_id);
// Проверяю пустое ли сердечко
    let cookies = convertStringToObject(document.cookie);
    if (current.src == path + 'static/icons/empty_heart.jpg') {
        current.src = 'static/icons/full_heart.jpg';

            if (cookies['UserCookie']){
                if (!cookies['UserCookie'].includes(String(prod_id))) {
                    let new_val = 'UserCookie=' + cookies['UserCookie'] + ':' + String(prod_id);
                    document.cookie = new_val;
             }

        }
        else {
            document.cookie = 'UserCookie=' + String(prod_id);


        }}
    else {
//        Реализовываем удаление
        current.src = 'static/icons/empty_heart.jpg';
        let old_val = cookies['UserCookie'].split(':');
        let new_val = []
        old_val.forEach(
        function(item, i, arr) {
        if (prod_id != Number(item)){
            new_val.push(String(item));
        }
        }

        )
        document.cookie = 'UserCookie=' + new_val.join(':');
         }
}







// Функция для добавления элемента в корзину
let addToCart = function(prod_id){
    let cookies = convertStringToObject(document.cookie);
    if (cookies['Cart']){
        cookies_list = [];
        cookies['Cart'].split(':').forEach(
        function(item, i, arr) {
            cookies_list.push(item.split('-')[0]);
        }
        )
        if (!cookies_list.includes(String(prod_id))) {
            let new_val = 'Cart=' + cookies['Cart'] + ':' + String(prod_id);
            console.log(new_val)
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
