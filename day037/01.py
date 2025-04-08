import requests

urls = ('http://baidu.com', 'http://souhu.com', 'http://sina.com')

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
