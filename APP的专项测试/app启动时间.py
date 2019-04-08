import os ,time,csv

class App():
    def __init__(self):
        self.content=''
        self.startTime=0
    def LaunchApp(self):
        cmd='adb shell am start -W -n com.chinacreditech.client/com.chinacreditech.client.SplashActivity'
        self.content=os.popen(cmd)

    def StopApp(self):
        cmd='adb shell am force-stop com.chinacreditech.client'
        #cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:

                self.startTime=line.split(':')[1]
               # print(self.startTime)
               # print(type(self.startTime))
                break

        return  self.startTime



class Controller():
    def __init__(self,count):
        self.app=App()
        self.counter=count
        self.alldata=[('elapsedtime','elpasedtime')]


    def testrprocess(self):
        self.app.LaunchApp()

        elpasedtime=self.app.GetLaunchedTime()

        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,elpasedtime))
        time.sleep(3)
        self.app.StopApp()
        time.sleep(5)

    def run(self):
        while self.counter>0:
            self.testrprocess()
            self.counter=self.counter-1
    def getCurrentTime(self):
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        #print(currentTime)
        #print(type(currentTime))
        return  currentTime


    def saveDataToCSV(self):
        csvfile=open('startTime.csv','w',encoding='utf-8')
        write=csv.writer(csvfile)
        write.writerows(self.alldata)
        #csvfile.writelines(self.alldata)

        csvfile.close()
if __name__=='__main__':
    controller=Controller(10)
    controller.run()
    controller.saveDataToCSV()

