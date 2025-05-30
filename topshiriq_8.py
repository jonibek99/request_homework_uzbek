import requests

"""
https://jsonplaceholder.typicode.com/posts manziliga
quyidagi ma'lumotlarni POST qilib yuboring:
{
    "title": "Mening sarlavham",
    "body": "Bu mening birinchi postim.",
    "userId": 1
}
Va javobdagi JSONni ko'rsating.
"""
response=requests.post('https://jsonplaceholder.typicode.com/posts',data={
    "title": "Mening sarlavham",
    "body": "Bu mening birinchi postim.",
    "userId": 1
})
print(response.json())

