import requests

"""
https://jsonplaceholder.typicode.com/todos/1 sahifasiga so'rov yuboring
va JSON javobini chiqarib bering.
"""
response=requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.json())