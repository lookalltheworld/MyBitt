import requests
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
ses=requests.session()
data={'email':'325*****@qq.com','password':'1234561a'}
ses.post('http://www.renren.com/PLogin.do',data=data)
response=ses.get('http://www.renren.com/880151247/profile')
print(response.text)