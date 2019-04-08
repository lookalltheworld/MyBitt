import urllib.request
import urllib
wd={'wd':'北京'}
url='http://www.baidu.com/s?'
wdd=urllib.parse.urlencode(wd)
print(wdd)
url=url + wdd


req=urllib.request.Request(url)

#reponse=opener.open(req).read().decode()

reponse=urllib.request.urlopen(req).read().decode()
print(reponse)