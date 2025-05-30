import requests

"""
https://jsonplaceholder.typicode.com/404 sahifasiga so'rov yuboring.
Agar sahifa topilmasa, foydalanuvchiga
"Xatolik: sahifa topilmadi" deb chiqaring.
"""
response=requests.get("https://jsonplaceholder.typicode.com/404")
if response.status_code!=200:
    print("Xatolik: sahifa topilmadi")
else:
    print(response.json())