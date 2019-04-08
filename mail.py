import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import report


def mail(name):
     #邮件信息配置. 授权码 xdclass123
     sender = '13978637441@163.com'
     receiver = 'lookalltheworld@163.com'
     auth_code = 'w123456'  #设置客户端授权码，不是密码

     smtpserver = 'smtp.163.com'
     subject = '自动化测试报告'


     #读取文件内容
     f = open("./report/"+name, 'rb')
     mail_body = f.read()
     f.close()



     #HTML 形式的文件内容
     html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
     html['Subject'] = subject
     html['from'] = sender
     html['to'] = receiver



     # html附件 将测试报告放在附件中发送
     att1 = MIMEText(mail_body, 'base64', 'gb2312')
     att1["Content-Type"] = 'application/octet-stream'
     att1["Content-Disposition"] = 'attachment; filename="XdclassTestReport.html"'  # 这里的filename可以任意写



     msg = MIMEMultipart()
     msg['Subject'] = subject  # 邮件的标题
     msg.attach(html)  # 将html附加在msg里
     msg.attach(att1)  # 新增一个附件



     #连接 登录 上smtp服务器
     smtp = smtplib.SMTP()
     smtp.connect('smtp.163.com')
     smtp.login(sender, auth_code)

     #发送邮件
     smtp.sendmail(sender, receiver, msg.as_string())
     smtp.quit()
