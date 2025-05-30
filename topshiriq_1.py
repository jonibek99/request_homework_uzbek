import requests

"""
https://example.com sahifasiga GET so'rov yuboring
va javob holatini (status_code) ekranga chiqaring.
"""
response=requests.get('https://example.com')
print(response.status_code)