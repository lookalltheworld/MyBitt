import unittest
import time,ddt
from common import read_execl
from business import login
from selenium.webdriver.support.ui import WebDriverWait
url=read_execl.read_excel('test_data/element.xlsx')

@ddt.ddt
class tractionMoney_class(unittest.TestCase):
    def setUp(self):
        self.driver=login.login()
    def tearDown(self):
        if self.driver:
            self.driver.quit()
    @ddt.unpack
    @ddt.data(*read_execl.read_excel_list('test_data/tractionAddress.xlsx'))
    def test_tractionMoney(self,name,mainCoinType,asset,receiveAddress,amout):
        mainCoinType=int(mainCoinType)
        asset=int(asset)
        amout=str(amout)
        passwd = int(url['passwd'])
        driver=self.driver
        # 交易
        driver.find_element_by_id(url['llTabMarket']).click()
        # 普通转帐
        driver.find_element_by_id(url['llTransCommon']).click()
        # 选资金类型
        driver.find_element_by_id(url['trMainCoinType']).click()
        # x=driver.get_window_size()['width']
        # y=driver.get_window_size()['height']
        # print(x,y)
        # size=driver.get_window_size()
        # print(size)
        time.sleep(2)
        if mainCoinType != 0:
            for i in range(mainCoinType):
                try:
                    time.sleep(1)
                    driver.swipe(0.5, 0.94, 0.5, 0.9)
                    #time.sleep(1)
                except:
                    pass
                # 确定

            driver.find_element_by_id(url['tvSure']).click()
        if asset !=0:
            #选资产
            driver.find_element_by_id(url['tvAsset']).click()
            for i in range(asset):
                try:
                    time.sleep(1)
                    driver.swipe(0.5, 0.94, 0.5, 0.9)
                    #time.sleep(1)
                except:
                    pass
        # 确定
        try:
           driver.find_element_by_id(url['tvSure']).click()

        except:
            pass
        # 选将资金类型中的币种
        driver.find_element_by_id(url['tvAsset']).click()
        driver.find_element_by_id(url['tvSure']).click()

        # 选择付款钱包
        driver.find_element_by_id(url['tvPayWallet']).click()
        driver.find_element_by_id(url['tvSure']).click()
        # 收款地址
        driver.find_element_by_id(url['etReceiveAddress']).send_keys(receiveAddress)
        #time.sleep(2)
        # 下一步
        WebDriverWait(driver,20).until(lambda x:x.find_element_by_id(url['btnNext']))
        driver.find_element_by_id(url['btnNext']).click()
        #time.sleep(4)
        # 转帐金额
        WebDriverWait(driver,20).until(lambda x:x.find_element_by_id(url['etAmount']))
        driver.find_element_by_id(url['etAmount']).send_keys(amout)
        # 备注
        ele2='转了{}{}'.format(amout,name)
        driver.find_element_by_id(url['etNote']).send_keys(ele2)
        # 点击核对转账信息
        driver.find_element_by_id(url['btnCheck']).click()
        # 确认转账
        WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id(url['btnSure']))
        driver.find_element_by_id(url['btnSure']).click()
        # 输入密码
        driver.find_element_by_id(url['etPwd']).send_keys(passwd)
        # 确定
        driver.find_element_by_id(url['tvSure']).click()
        #time.sleep(30)
        WebDriverWait(driver,60).until(lambda x:x.find_element_by_id(url['tvState']))
        last_text = driver.find_element_by_id(url['tvState']).text
        self.assertEqual('交易等待中',last_text)
        #if last_text == '交易等待中':
        #    print('发送成功：', last_text)