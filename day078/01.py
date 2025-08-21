import requests

resp = requests.get('https://www.sina.com/')
if resp.status_code == 200:
    print(resp.text)