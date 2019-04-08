import requests
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
wd={'wd':'java'}
proxy={'http':'http://101.248.64.72:8080'}
response=requests.get('http://www.baidu.com/s?',params=wd,headers=headers,proxies=proxy)
data=response.content
print(data.decode())