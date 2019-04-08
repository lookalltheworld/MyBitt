import unittest
from business import login
import time,ddt
from common import read_execl
from selenium.webdriver.support.ui import WebDriverWait
url=read_execl.read_excel('test_data/element.xlsx')
@ddt.ddt
class creatWallet_class(unittest.TestCase):
    def setUp(self):
        self.driver=login.login()
    def tearDown(self):
        if self.driver:
            self.driver.quit()
    @ddt.unpack
    @ddt.data(*read_execl.read_excel_list('test_data/createWallet.xlsx'))
    def test_creatWallet(self,wallet,walletName):
        passwd=int(url['passwd'])
        passwd1 = int(url['passwd1'])

        #print('wallet:',wallet)
        #print('walletName:', walletNane)
        #print(passwd)
        driver=self.driver

        #管理
        driver.find_element_by_id(url['manage']).click()
        # 钱包管理
        driver.find_element_by_xpath(url['wallet_manage']).click()
        # +钱包
        driver.find_element_by_id(url['add_wallet']).click()
        # 开始使用
        # driver.find_element_by_id('com.machain.mybitt:id/btnIn').click()
        # 创建钱包
        driver.find_element_by_id(url['CreateWallet']).click()
        # 跳过
        driver.find_element_by_id(url['menuSkip']).click()
        # 创建ETH
        nan='//*[@text="{}"]'.format(wallet)
        #print(nan,wallet,walletNane)
        try:
            driver.find_element_by_xpath(nan).click()
        except:
            try:
                driver.swipe(0.5, 0.9, 0.5, 0.2, 1000)
            except:
                pass
            driver.find_element_by_xpath(nan).click()
        #driver.find_element_by_xpath(nan).click()

        if wallet =='NEO'or wallet=='NEO(Test)':
            WebDriverWait(driver,300).until(lambda x:x.find_element_by_id(url['etPwd']))
            driver.find_element_by_id(url['etPwd']).send_keys(passwd1)
            driver.find_element_by_id(url['btnNext']).click()
        # 热钱包名称
        WebDriverWait(driver, 300).until(lambda x: x.find_element_by_id(url['etName']))

        driver.find_element_by_id(url['etName']).send_keys(walletName)
        # 交易密码
        driver.find_element_by_id(url['etPwd']).send_keys(passwd)
        # 复核密码
        driver.find_element_by_id(url['etPwdSure']).send_keys(passwd)
        # 同意协议
        driver.find_element_by_id(url['cbAgreement']).click()
        # 创建完成
        driver.find_element_by_id(url['btnCreateWallet']).click()
        #time.sleep(5)
        # 暂不备份，先用用看
        #driver.find_element_by_id(url['btnContinueAddAddress']).click()
        WebDriverWait(driver,300).until(lambda x:x.find_element_by_id(url['btnContinueAddAddress']))
        driver.find_element_by_id(url['btnContinueAddAddress']).click()
        time.sleep(1)
        # 我就不
        driver.find_element_by_id(url['btnCancel']).click()
        time.sleep(1)
        # 我不在乎
        # driver.find_element_by_id('com.machain.mybitt:id/btnCancel').click()
        # time.sleep(2)
        try:
            driver.find_element_by_id(url['btnCancel']).click()
        except:
            pass
        # 判定钱是否是0
        ele = driver.find_element_by_id(url['tvTotalMoney'])
        money = ele.text
        money1 = 0
        if money == '0' or money=='-':

            print('没钱')
        else:
            money1=8
            print('有钱：%s'.format(money))

        # 管理
        driver.find_element_by_id(url['manage']).click()
        # 钱包管理
        driver.find_element_by_xpath(url['wallet_manage']).click()
        # 点击1111钱包
        try:
           driver.find_element_by_xpath(nan).click()
        except:
            try:
                driver.swipe(0.5,0.9,0.5,0.2,1000)
            except:
                pass
            driver.find_element_by_xpath(nan).click()
        # 删除钱包
        driver.find_element_by_id(url['btnDelete']).click()
        # 输入密码
        driver.find_element_by_id(url['etPwd']).send_keys(passwd)
        # 确认
        driver.find_element_by_id(url['tvSure']).click()
        WebDriverWait(driver, 300).until(lambda x: x.find_element_by_id(url['btnDelete']))
        # 钱不为0时，截图和打印

        if money1 == 8:
            driver.save_screenshot(str(time.time()) + '.png')
            if wallet =='XMC':
                a1=driver.find_element_by_id(url['tvAddress'])
                a2=driver.find_element_by_id(url['tvViewKey'])
                a3=driver.find_element_by_id(url['tvSpendKey'])
                print('XMC钱包地址:',a1.text)
                print('XMC只读私钥:', a2.text)
                print('XMC花费私钥:', a3.text)
            else:
                ele1 = driver.find_element_by_id(url['tvKey'])
                print(wallet,':',ele1.text)

            print('一共有钱：',money,'___________________________________________________________________________________________________________________________________________')


        #time.sleep(18)
        #try:
        #    ele1 = driver.find_element_by_id(url['tvKey'])
        #    print(wallet,': ',ele1.text)
        #except:
        #    pass
        # 删除钱包1

        time.sleep(3)
        driver.find_element_by_id(url['btnDelete']).click()
        time.sleep(1)
        # 确定
        driver.find_element_by_id(url['btnSure']).click()