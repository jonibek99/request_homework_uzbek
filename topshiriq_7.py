import requests

"""
https://jsonplaceholder.typicode.com/comments sahifasiga
`postId=1` parametrini yuboring va natijani ko'rsating.
"""
response=requests.get("https://jsonplaceholder.typicode.com/comments",params={'postId':1}).json()
print(response)
