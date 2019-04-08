import subprocess
import time,multiprocessing

def start_appium(host,port):
    bootstrap_port=port+1
    cmd='start /b appium -a %s -p %s -bp %s'%(host,str(port),str(bootstrap_port))
    print(cmd,'启动时间',time.ctime())
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

appium_process=[]
for i in range(2):
    host='127.0.0.1'
    port=4723+i*2
    appium=multiprocessing.Process(target=start_appium,args=(host,port))
    appium_process.append(appium)
if __name__=='__main__':
    #host='127.0.0.1'
    #port=4723
    #start_appium(host,port)
    for i in appium_process:
        i.start()
    for j in appium_process:
        j.join()