import urllib.request
import random
proxylist=[
    {'http':'209.203.130.51:8080'},
    {'http':'111.177.170.245:9999'}
]
proxy=random.choice(proxylist)
print(proxy)
proxyHandler=urllib.request.ProxyHandler(proxy)
opener=urllib.request.build_opener(proxyHandler)

req=urllib.request.Request('http://www.baidu.com')

reponse=opener.open(req).read().decode()
#urllib.request.install_opener(opener)
#reponse=urllib.request.urlopen(req).read().decode()
print(reponse)