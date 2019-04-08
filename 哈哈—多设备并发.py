import time ,multiprocessing
#coding=utf-8
from appium import webdriver
devices_list=['127.0.0.1:62001','127.0.0.1:62025']
def app_start(udid,port):
     desired_caps = {}
     desired_caps['platformName'] = 'Android'
     desired_caps['platformVersion'] = '7'
     desired_caps['deviceName'] = 'Android'
     desired_caps['appPackage'] = 'com.gl365.android.merchant'
     desired_caps['appActivity'] = '.MainActivity'
     desired_caps['unicodeKeyboard'] = True
     desired_caps['resetKeyboard'] = True
     desired_caps['udid'] = udid
     #保持登录状态
     #desired_caps['noReset'] = 'True'
     desired_caps['newCommandTimeout'] = '6000'
     #desired_caps['automationName'] = 'uiautomator2'

     #android.widget.ImageView
     print('appium port:%s start run %s at %s'%(port,udid,time.ctime()))
     driver = webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub', desired_caps)
     driver.implicitly_wait(10)
desired_process=[]
for i in range(len(devices_list)):
    port=4723 +2*i
    desired=multiprocessing.Process(target=app_start,args=(devices_list[i],port))
    desired_process.append(desired)
if __name__=='__main__':
    #app_start(devices_list[0],4723)
    #app_start(devices_list[1],4725)
    for j in desired_process:
        j.start()
    for n in desired_process:
        n.join()
#time.sleep(5)
#driver.swipe(0.9,0.5,0.1,0.5,1000)
#time.sleep(2)
#driver.swipe(0.9,0.5,0.1,0.5,1000)
#time.sleep(1)
#driver.find_element_by_id('com.gl365.android.merchant:id/go_to').click()
#print(driver.contexts)
##for contextName in driver.contexts:
##  if 'WebView' in contextName:
##      driver.switch_to.context(contextName)
#time.sleep(1)
#driver.find_element_by_xpath('//android.widget.EditText[@index="0"]').send_keys('671000165')
#time.sleep(1)
#driver.find_element_by_xpath('//android.widget.EditText[@index="2"]').send_keys('a12345678')
#time.sleep(1)
#driver.find_element_by_accessibility_id('登 录').click()
#time.sleep(2)