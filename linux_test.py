#import paramiko
#远程执行命令
#ssh_client=paramiko.SSHClient()
#
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#ssh_client.connect('192.168.74.131',22,'root','123456')
#
#stdin,stdout,stderr = ssh_client.exec_command("touch a.txt")
#L=[]
#l=stdout.readlines()
#for i in l:
#    a=i.replace('\n','')
#    L.append(a)
#print(L)
#
#ssh_client.close()


#下载和上传文件
import paramiko,time
import os
import sys

hostname='192.168.74.131'
username='root'
password='123456'
port=22

t = paramiko.Transport((hostname, port))
t.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(t)


#sftp.get('/root/a.txt','C:/Users/53294/Desktop/load/a.txt')#下载文件
a=time.time()
sftp.put('C:/Users/53294/Desktop/load/CentOS-7-x86_64-Minimal-1804.iso','/root/CentOS-7-x86_64-Minimal-1804.iso') #上传文件
b=time.time()
print(a,'\n',b,'\n',b-a)
t.close()
