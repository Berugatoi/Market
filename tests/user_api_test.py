from requests import put, post, delete, get
from datetime import date


user1 = {"name": "Zelimkhan", "surname": "Guchiev", 'email': "vip.guchiev@mail.ru",
         "birthday": date(2004, 6, 4).__str__(), 'created_date': date.today().__str__(),
         'password': "abcdef12345"}

url1 = "http://127.0.0.1:5000/api/user"
# res1 = post(url1, data=user1)
# print(res1)

# res2 = get(url1).json()
# print(res2)


res4 = delete(url1 + "/1")
print(res4)

res3 = get(url1 + "/1").json()
print(res3)

