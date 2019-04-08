import unittest
from business import login
import time,ddt
from common import read_execl
from selenium.webdriver.support.ui import WebDriverWait
from business import delete_wallet

url=read_execl.read_excel('test_data/element.xlsx')
@ddt.ddt
class importWallet_class(unittest.TestCase):
    def setUp(self):
        self.driver=login.login()
    def tearDown(self):
        if self.driver:
            self.driver.quit()
    @ddt.unpack
    @ddt.data(*read_execl.read_excel_list('test_data/walletAddress.xlsx'))
    def test_importWallet(self,wallet,walletName,private_key):
        driver=self.driver
        passwd = int(url['passwd'])
        passwd1 = int(url['passwd1'])

        # print('wallet:',wallet)
        # print('walletName:', walletNane)
        # print(passwd)
        driver = self.driver

        # 管理
        driver.find_element_by_id(url['manage']).click()
        # 钱包管理
        driver.find_element_by_xpath(url['wallet_manage']).click()
        # +钱包
        driver.find_element_by_id(url['add_wallet']).click()
        time.sleep(2)
        # 导入钱包
        driver.find_element_by_id(url['btnImportWallet']).click()
        # 跳过
        driver.find_element_by_id(url['menuSkip']).click()
        nan = '//*[@text="{}"]'.format(wallet)
        try:
            driver.find_element_by_xpath(nan).click()
        except:
            try:
                driver.swipe(0.5, 0.9, 0.5, 0.2, 1000)
            except:
                pass
            driver.find_element_by_xpath(nan).click()

        driver.find_element_by_xpath(url['show_passwd']).click()
        # 输入私钥
        driver.find_element_by_id(url['etWords']).send_keys(private_key)
        if wallet=='NEO'or wallet=='NEO(Test)':
            driver.find_element_by_id(url['etPwd']).send_keys(passwd1)
        # 同意协议
        driver.find_element_by_id(url['cbAgreement']).click()
        # 开始导入
        driver.find_element_by_id(url['btnLoad']).click()
        # 热钱包名称
        WebDriverWait(driver, 300).until(lambda x: x.find_element_by_id(url['etName']))

        driver.find_element_by_id(url['etName']).send_keys(walletName)
        # 交易密码
        driver.find_element_by_id(url['etPwd']).send_keys(passwd)
        # 复核密码
        driver.find_element_by_id(url['etPwdSure']).send_keys(passwd)

        # 创建完成
        driver.find_element_by_id(url['btnCreateWallet']).click()
        #time.sleep(4)
        # 进入钱包，开始使用
        WebDriverWait(driver, 300).until(lambda x: x.find_element_by_id(url['btnStartUse']))
        driver.find_element_by_id(url['btnStartUse']).click()
        #删除钱包
        delete_wallet.delete_wallet(driver,url,nan,passwd)