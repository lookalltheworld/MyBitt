from appium import  webdriver
import time

appium_url='http://192.168.1.211:4723/wd/hub'
desired_capabilities = {
    'platformName': 'Android',
    "platformVersion": '7',
    "deviceName": '127.0.0.1:62025',
    "appPackage": "com.machain.mybitt",
    "appActivity": "com.machain.module.main.ui.welcome.WelcomeActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "automationName":"uiautomator2",
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
##开始使用
#driver.find_element_by_id('com.machain.mybitt:id/btnIn').click()
#管理
driver.find_element_by_id('com.machain.mybitt:id/llTabManage').click()
#钱包管理
driver.find_element_by_xpath('//*[@text="钱包管理"]').click()
#+钱包
driver.find_element_by_id('com.machain.mybitt:id/menuAdd').click()
#导入钱包
driver.find_element_by_id('com.machain.mybitt:id/btnImportWallet').click()
#跳过
driver.find_element_by_id('com.machain.mybitt:id/menuSkip').click()
#选择ETH
driver.find_element_by_xpath('//*[@text="ETH"]').click()

driver.find_element_by_xpath('//*[@text="明文私钥导入"]').click()
#输入私钥
driver.find_element_by_id('com.machain.mybitt:id/etWords').send_keys('0xab35455b3dc8b9ab3e0bab906e8cb12419b9b6ddeef42e86cf44375020e2e18c')
#同意协议
driver.find_element_by_id('com.machain.mybitt:id/cbAgreement').click()
#开始导入
driver.find_element_by_id('com.machain.mybitt:id/btnLoad').click()
#热钱包名称
driver.find_element_by_id('com.machain.mybitt:id/etName').send_keys('2222')
#交易密码
driver.find_element_by_id('com.machain.mybitt:id/etPwd').send_keys('123456')
#复核密码
driver.find_element_by_id('com.machain.mybitt:id/etPwdSure').send_keys('123456')
#完成导入
driver.find_element_by_id('com.machain.mybitt:id/btnCreateWallet').click()
time.sleep(4)
#进入钱包，开始使用
driver.find_element_by_id('com.machain.mybitt:id/btnStartUse').click()
#管理
driver.find_element_by_id('com.machain.mybitt:id/llTabManage').click()
#钱包管理
driver.find_element_by_xpath('//*[@text="钱包管理"]').click()

#driver.swipe(0.5,0.9,0.5,0.1,1000)
#点击2222钱包
driver.find_element_by_xpath('//*[@text="2222"]').click()
#删除钱包
driver.find_element_by_id('com.machain.mybitt:id/btnDelete').click()
#输入密码
driver.find_element_by_id('com.machain.mybitt:id/etPwd').send_keys('123456')
#确认
driver.find_element_by_id('com.machain.mybitt:id/tvSure').click()
time.sleep(18)
#删除钱包1
driver.find_element_by_id('com.machain.mybitt:id/btnDelete').click()
time.sleep(2)
#确定
driver.find_element_by_id('com.machain.mybitt:id/btnSure').click()