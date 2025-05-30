import requests

"""
https://jsonplaceholder.typicode.com/users manzilidan
foydalanuvchilar ro'yxatini oling va
ularning ismlarini chiqarib bering.
"""
response=requests.get("https://jsonplaceholder.typicode.com/users")
data=response.json()
for i in data:
    print(i['name'])
