import requests

"""
3-topshiriqdagi JSON javobdan "title" maydonini
ajratib olib konsolga chiqaring.
"""
res=requests.get('https://jsonplaceholder.typicode.com/todos/1')
data=res.json()
print(data['title'])