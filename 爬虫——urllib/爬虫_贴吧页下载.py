import urllib.request
import urllib,time
#https://tieba.baidu.com/f?kw=%E9%81%93%E5%90%9B&ie=utf-8&pn=0
#https://tieba.baidu.com/f?kw=%E9%81%93%E5%90%9B&ie=utf-8&pn=50
#https://tieba.baidu.com/f?kw=%E9%81%93%E5%90%9B&ie=utf-8&pn=100
def load_b(url):
    print('正在下载……')
    req=urllib.request.Request(url)
    response=urllib.request.urlopen(req).read()
    return response

def save_b(file_name,html):
    print('正在保存……')
    with open(file_name,'wb') as f:
        f.write(html)

def tiebaSpider(url,begin,end):
    for i in range(begin,end+1):
        page=(i-1)*50
        url=url+'&ie=utf-8&pn={}'.format(page)
        file_name='d:/第{}页.html'.format(str(i))
        html=load_b(url)
        save_b(file_name,html)


if __name__ =='__main__':
    kw=input('请输入贴吧名称：')
    begin=int(input('请输开始页：'))
    end=int(input('请输入结束页：'))
    url='https://tieba.baidu.com/f?'
    kw=urllib.parse.urlencode({'kw':kw})
    url=url + kw
    tiebaSpider(url,begin,end)
    time.sleep(5)

