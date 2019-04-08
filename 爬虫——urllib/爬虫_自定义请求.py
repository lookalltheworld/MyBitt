import urllib.request
http_hander=urllib.request.HTTPHandler()

opener=urllib.request.build_opener(http_hander)

req=urllib.request.Request('http://www.baidu.com')

#reponse=opener.open(req).read().decode()
urllib.request.install_opener(opener)
reponse=urllib.request.urlopen(req).read().decode()
print(reponse)