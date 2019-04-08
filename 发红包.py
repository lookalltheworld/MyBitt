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
#管理
driver.find_element_by_id('com.machain.mybitt:id/llTabManage').click()
#点击MyBitt
driver.find_element_by_id('com.machain.mybitt:id/manage_user_center').click()
try:
     #手机号
     driver.find_element_by_id('com.machain.mybitt:id/login_phone').send_keys('13800138000')
     ##下一步
     driver.find_element_by_id('com.machain.mybitt:id/login_next').click()
     ##发送验证码
     driver.find_element_by_id('com.machain.mybitt:id/send_code').click()
     ##登录
     driver.find_element_by_id('com.machain.mybitt:id/login_or_register').click()
except:
    pass
#返回
driver.find_element_by_class_name('android.widget.ImageButton').click()
#交易
driver.find_element_by_id('com.machain.mybitt:id/llTabMarket').click()
#发红包
driver.find_element_by_id('com.machain.mybitt:id/llRedPocket').click()

#选币种
driver.find_element_by_id('com.machain.mybitt:id/trSelectToken').click()
time.sleep(2)
#选ETH(Test)
coinType='ETH(Test'
driver.find_element_by_xpath('//*[@resource-id="com.machain.mybitt:id/tvCoinTypeName" and @text="ETH"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@resource-id="com.machain.mybitt:id/tvCoinTypeName" and @text="BTC(Test)"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@resource-id="com.machain.mybitt:id/tvCoinTypeName" and @text="ETH(Test)"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@resource-id="com.machain.mybitt:id/tvCoinTypeName" and @text="VNS"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@resource-id="com.machain.mybitt:id/tvCoinTypeName" and @text="BCH(Test)"]').click()
ele_click='//*[@resource-id="com.machain.mybitt:id/tvCoinTypeName" and @text="{}"]'.format(coinType)
driver.find_element_by_xpath(ele_click).click()
i=0
while i<10 :
    i=i+1
    try:
        ele=driver.find_element_by_xpath('//*[@resource-id="com.machain.mybitt:id/tvTokenName" and @text ="USDT（Test）"]')
        ele.click()
        break
       # and@text ="USDT（Test）"
    except:
        driver.swipe(0.5,0.95,0.5,0.1,1000)
        pass
#eles=driver.find_elements_by_id('com.machain.mybitt:id/tvTokenName')
#eles[0].click()
#小白发红包
driver.find_element_by_id('com.machain.mybitt:id/tvSmall').click()
#金额
driver.find_element_by_id('com.machain.mybitt:id/etAmount').send_keys('0.1')
#人数
driver.find_element_by_id('com.machain.mybitt:id/etPeopleNum').send_keys('2')
#下一步
driver.find_element_by_id('com.machain.mybitt:id/btnNext').click()

time.sleep(5)
#立即支付
driver.find_element_by_id('com.machain.mybitt:id/btnPay').click()
#选钱包
driver.find_element_by_id('com.machain.mybitt:id/tvWalletName').click()
driver.find_element_by_id('com.machain.mybitt:id/ivSelect').click()

#输入密码
driver.find_element_by_id('com.machain.mybitt:id/etPwd').send_keys('123456')
#按回车
driver.press_keycode('66')
time.sleep(60)
ele1=driver.find_element_by_id('com.machain.mybitt:id/tvTip')
textLast=ele1.text
if textLast=='大红包已生成，尽快分享哦~':
    print('发红包成功：',textLast)