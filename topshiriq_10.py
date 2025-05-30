import requests

"""
https://api.agify.io?name=sanjarbek manzilidan
foydalanuvchining taxminiy yoshini oling.
Natijani quyidagicha chiqaring:
"Ism: sanjarbek, Taxminiy yosh: 25"
"""
response=requests.get('https://api.agify.io',params={'name':'sanjarbek'})
data=response.json()
print(f'Ism: {data['name']},Taxminiy yosh: {data['age']}')