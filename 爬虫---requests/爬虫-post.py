import requests
headers={
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'Cookie': '_ntes_nnid=c79e4db49ad2b5fe59cfb51431e4d0bb,1522472828907; OUTFOX_SEARCH_USER_ID_NCOO=806223821.1234775; OUTFOX_SEARCH_USER_ID=-1222678520@10.168.11.12; P_INFO=lookalltheworld@163.com|1526784112|2|mail163|11&19|gud&1526621851&mail163#gud&440300#10#0#0|139441&0|kaola&ecard&mail163&blog|lookalltheworld@163.com; JSESSIONID=aaaruekupKcYM5rjgUjMw; ___rl__test__cookies=1552796636381',
'Referer': 'http://fanyi.youdao.com/'
}
key='你好'
data={
'i':key,
'from': 'AUTO',
'to':'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt':'15527937727790',
'sign': 'b940150590f5eb9b345101768c8dfd8c',
'ts': '1552793772779',
'bv': '9c4fffad2fb69d08cd130e408e0f8108',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTlME',
'typoResult': 'false'
}
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

response=requests.post(url,data=data,headers=headers)
data=response.text
print(data)