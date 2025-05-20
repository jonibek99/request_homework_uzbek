🏠 Python requests kutubxonasi bo‘yicha 10 ta uyga vazifa (O‘zbek tilida)

1. Topshiriq – Saytga so‘rov yuboring
python
CopyEdit
# https://example.com sahifasiga GET so‘rov yuboring va javob holatini (status_code) ekranga chiqaring.


2. Topshiriq – Sayt matnini ko‘rish
python
CopyEdit
# https://example.com sahifasiga GET so‘rov yuboring va javob matnini (text) konsolga chiqaring.


3. Topshiriq – JSON javobni chiqarish
python
CopyEdit
# https://jsonplaceholder.typicode.com/todos/1 sahifasiga so‘rov yuboring va JSON javobini chiqarib bering.


4. Topshiriq – Muayyan qiymatni olish
python
CopyEdit
# 3-topshiriqdagi JSON javobdan "title" maydonini ajratib olib konsolga chiqaring.


5. Topshiriq – Foydalanuvchilar ro‘yxatini olish
python
CopyEdit
# https://jsonplaceholder.typicode.com/users manzilidan foydalanuvchilar ro‘yxatini oling va ularning ismlarini chiqarib bering.


6. Topshiriq – Foydalanuvchilarni sanash
python
CopyEdit
# 5-topshiriqdagi ro‘yxat nechta foydalanuvchidan iborat ekanligini hisoblang va konsolga chiqaring.


7. Topshiriq – Parametr bilan GET so‘rov
python
CopyEdit
# https://jsonplaceholder.typicode.com/comments sahifasiga `postId=1` parametrini yuboring va natijani ko‘rsating.


8. Topshiriq – POST so‘rov yuborish
python
CopyEdit
# https://jsonplaceholder.typicode.com/posts manziliga quyidagi ma’lumotlarni POST qilib yuboring:
# {
#     "title": "Mening sarlavham",
#     "body": "Bu mening birinchi postim.",
#     "userId": 1
# }
# Va javobdagi JSONni ko‘rsating.


9. Topshiriq – Xatolikni tekshirish
python
CopyEdit
# https://jsonplaceholder.typicode.com/404 sahifasiga so‘rov yuboring.
# Agar sahifa topilmasa, foydalanuvchiga "Xatolik: sahifa topilmadi" deb chiqaring.


10. Topshiriq – Boshqa APIdan ma’lumot olish
python
CopyEdit
# https://api.agify.io?name=sanjarbek manzilidan foydalanuvchining taxminiy yoshini oling.
# Natijani quyidagicha chiqaring:
# "Ism: sanjarbek, Taxminiy yosh: 25"

