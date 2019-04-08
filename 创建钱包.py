from appium import  webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

appium_url='http://127.0.0.1:4723/wd/hub'
desired_capabilities = {
    'platformName': 'Android',
    "platformVersion": '7',
    "deviceName": 'android',
    "appPackage": "com.machain.mybitt",
    "appActivity": "com.machain.module.main.ui.welcome.WelcomeActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "automationName": "uiautomator2",
    "newCommandTimeout": 6000
}

driver = webdriver.Remote(
    command_executor=appium_url,
    desired_capabilities=desired_capabilities
)

# 隐式等待
driver.implicitly_wait(10)
#driver.swipe(0.9,0.5,0.1,0.5)
#driver.swipe(0.9,0.5,0.1,0.5)
#driver.swipe(0.9,0.5,0.1,0.5)
driver.find_element_by_id('com.machain.mybitt:id/llTabManage').click()
#钱包管理
driver.find_element_by_xpath('//*[@text="钱包管理"]').click()
#+钱包
driver.find_element_by_id('com.machain.mybitt:id/menuAdd').click()
#开始使用
#driver.find_element_by_id('com.machain.mybitt:id/btnIn').click()
#创建钱包
driver.find_element_by_id('com.machain.mybitt:id/btnCreateWallet').click()
#跳过
driver.find_element_by_id('com.machain.mybitt:id/menuSkip').click()
#创建ETH
driver.find_element_by_xpath('//*[@text="ETH(Test)"]').click()
#热钱包名称
driver.find_element_by_id('com.machain.mybitt:id/etName').send_keys('1111')
#交易密码
driver.find_element_by_id('com.machain.mybitt:id/etPwd').send_keys('123456')
#复核密码
driver.find_element_by_id('com.machain.mybitt:id/etPwdSure').send_keys('123456')
#同意协议
driver.find_element_by_id('com.machain.mybitt:id/cbAgreement').click()
#创建完成
driver.find_element_by_id('com.machain.mybitt:id/btnCreateWallet').click()
#time.sleep(5)
#暂不备份，先用用看
WebDriverWait(driver,30).until(lambda x:x.find_element_by_id('com.machain.mybitt:id/btnContinueAddAddress'))
driver.find_element_by_id('com.machain.mybitt:id/btnContinueAddAddress').click()
time.sleep(1)
#我就不
driver.find_element_by_id('com.machain.mybitt:id/btnCancel').click()
time.sleep(1)
#我不在乎
#driver.find_element_by_id('com.machain.mybitt:id/btnCancel').click()
#time.sleep(2)
#判定钱是否是0
ele=driver.find_element_by_id('com.machain.mybitt:id/tvTotalMoney')
money=ele.text
money1=0
if money=='0'or money=='-':

    print('没钱')
else:
    money1=8
    print('有钱：{}'.format(money))

#管理
driver.find_element_by_id('com.machain.mybitt:id/llTabManage').click()
#钱包管理
driver.find_element_by_xpath('//*[@text="钱包管理"]').click()
#点击1111钱包
driver.find_element_by_xpath('//*[@text="1111"]').click()
#删除钱包
driver.find_element_by_id('com.machain.mybitt:id/btnDelete').click()
#输入密码
driver.find_element_by_id('com.machain.mybitt:id/etPwd').send_keys('123456')
#确认
driver.find_element_by_id('com.machain.mybitt:id/tvSure').click()
#钱不为0时，截图和打印
if money1==8:
    ele1=driver.find_element_by_id('com.machain.mybitt:id/tvKey')
    driver.save_screenshot(str(time.time())+'.png')
    print('一共有钱：', money,'___________________________________________________________________________________________________________________________________________')

    print(ele1.text)

#删除钱包1
WebDriverWait(driver,30).until(lambda x:x.find_element_by_id('com.machain.mybitt:id/btnDelete'))
time.sleep(3)
driver.find_element_by_id('com.machain.mybitt:id/btnDelete').click()
time.sleep(1)
#确定
driver.find_element_by_id('com.machain.mybitt:id/btnSure').click()