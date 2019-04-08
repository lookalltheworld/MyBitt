import urllib.request
import re
import random
url='http://www.baidu.com/'
agent1='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
agent2='Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
agent3='Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
agent4='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
agent5='Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
agent6='Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
agent7='Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'
agent8='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
agent9='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
agent10='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
agent_list=[agent1,agent2,agent3,agent4,agent5,agent6,agent7,agent8,agent9,agent10]
agent=random.choice(agent_list)
print(agent)
header={
"User-Agent": agent
}
req=urllib.request.Request(url,headers=header)
response=urllib.request.urlopen(req).read().decode()
#print(response)
print(len(response))
print(type(response))
par=r'<title>(.*?)</title>'
data=re.findall(par,response)
print(data)