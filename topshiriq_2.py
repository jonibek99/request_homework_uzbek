import requests

"""
https://example.com sahifasiga GET so'rov yuboring
va javob matnini (text) konsolga chiqaring.
"""
respone=requests.get('https://example.com')
print(respone.text)