import os ,time,csv


class Controller():
    def __init__(self,count):
        self.counter=count
        self.alldata=[('elapsedtime','cpuvalue')]


    def testrprocess(self):
        result=os.popen('adb shell dumpsys cpuinfo|find "com.chinacreditech.client"')
        for line in result.readlines():
            if "com.chinacreditech.client" in line:
                  cpuvalue=line.split('%')[0]
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,cpuvalue))


    def run(self):
        while self.counter>0:
            self.testrprocess()
            self.counter=self.counter-1
            time.sleep(2)
    def getCurrentTime(self):
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        #print(currentTime)
        #print(type(currentTime))
        return  currentTime


    def saveDataToCSV(self):
        csvfile=open('cpuvalue.csv','w',encoding='utf-8')
        write=csv.writer(csvfile)
        write.writerows(self.alldata)
        #csvfile.writelines(self.alldata)

        csvfile.close()
if __name__=='__main__':
    controller=Controller(10)
    controller.run()
    controller.saveDataToCSV()

