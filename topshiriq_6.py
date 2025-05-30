import requests

"""
5-topshiriqdagi ro'yxat nechta foydalanuvchidan
iborat ekanligini hisoblang va konsolga chiqaring.
"""
res=requests.get('https://jsonplaceholder.typicode.com/users').json()
print(len(res))