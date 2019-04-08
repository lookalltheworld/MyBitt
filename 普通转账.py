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
#交易
driver.find_element_by_id('com.machain.mybitt:id/llTabMarket').click()
#普通转帐
driver.find_element_by_id('com.machain.mybitt:id/llTransCommon').click()
#选资金类型
driver.find_element_by_id('com.machain.mybitt:id/trMainCoinType').click()
#x=driver.get_window_size()['width']
#y=driver.get_window_size()['height']
#print(x,y)
#size=driver.get_window_size()
#print(size)
time.sleep(1)
for i in range(3):
    try:
      driver.swipe(0.5,0.94,0.5,0.9)
      time.sleep(1)
    except:
        pass
#确定
driver.find_element_by_id('com.machain.mybitt:id/tvSure').click()
#选将资金类型中的币种
driver.find_element_by_id('com.machain.mybitt:id/tvAsset').click()
driver.find_element_by_id('com.machain.mybitt:id/tvSure').click()

#选择钱包
driver.find_element_by_id('com.machain.mybitt:id/tvPayWallet').click()
driver.find_element_by_id('com.machain.mybitt:id/tvSure').click()
#收款地址
driver.find_element_by_id('com.machain.mybitt:id/etReceiveAddress').send_keys('0xabe3c05b42f58e2b35f68bc6bd65700b0d61ae97')
#下一步
driver.find_element_by_id('com.machain.mybitt:id/btnNext').click()
time.sleep(4)
#转帐金额
driver.find_element_by_id('com.machain.mybitt:id/etAmount').send_keys('0.1')
#备注
driver.find_element_by_id('com.machain.mybitt:id/etNote').send_keys('转了0.1ETH')
#点击核对转账信息
driver.find_element_by_id('com.machain.mybitt:id/btnCheck').click()
#确认转账
driver.find_element_by_id('com.machain.mybitt:id/btnSure').click()
#输入密码
driver.find_element_by_id('com.machain.mybitt:id/etPwd').send_keys('123456')
#确定
driver.find_element_by_id('com.machain.mybitt:id/tvSure').click()
time.sleep(30)
last_text=driver.find_element_by_id('com.machain.mybitt:id/tvState').text
if last_text == '交易等待中':
    print('发送成功：',last_text)