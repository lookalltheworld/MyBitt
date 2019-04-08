import unittest
import time,ddt
from common import read_execl
from business import login,red_chose_coin
from selenium.webdriver.support.ui import WebDriverWait


url=read_execl.read_excel('test_data/element.xlsx')

@ddt.ddt
class sendMoney_class(unittest.TestCase):
    def setUp(self):
        self.driver=login.login()
    def tearDown(self):
        if self.driver:
            self.driver.quit()
    @ddt.unpack
    @ddt.data(*read_execl.read_excel_list('test_data/send_money.xlsx'))
    def test_sendMoney(self,phone,coinType,coin,coin_amount,people_num,red_pocket_large_or_samall):
        driver=self.driver
        passwd = int(url['passwd'])
        coin_amount=str(coin_amount)
        phone=int(phone)
        people_num=int(people_num)

        driver.find_element_by_id(url['manage']).click()
        # 点击MyBitt
        driver.find_element_by_id(url['manage_user_center']).click()
        try:
            # 手机号
            driver.find_element_by_id(url['login_phone']).send_keys(phone)
            ##下一步
            driver.find_element_by_id(url['login_next']).click()
            ##发送验证码
            driver.find_element_by_id(url['send_code']).click()
            ##登录
            driver.find_element_by_id(url['login_or_register']).click()
        except:
            pass
        # 返回
        driver.find_element_by_class_name(url['ImageButton']).click()
        # 交易
        driver.find_element_by_id(url['llTabMarket']).click()
        # 发红包
        driver.find_element_by_id(url['llRedPocket']).click()
        if red_pocket_large_or_samall=='small':
             #点小白发红包
             driver.find_element_by_id('com.machain.mybitt:id/tvSmall').click()

        # 选币种
        #driver.find_element_by_id(url['trSelectToken']).click()
        ##time.sleep(2)
        ## 选ETH(Test)
        #WebDriverWait(driver,10).until(lambda x:x.find_elements_by_id(url['tvTokenName']))
        #ele = driver.find_elements_by_id(url['tvTokenName'])
        #ele[coin].click()
        red_chose_coin.red_chose_coin(driver,url,coinType,coin)
        # 金额
        driver.find_element_by_id(url['etAmount']).send_keys(coin_amount)
        # 人数
        driver.find_element_by_id(url['etPeopleNum']).send_keys(people_num)
        # 下一步
        driver.find_element_by_id(url['btnNext']).click()
        #time.sleep(4)

        # 立即支付
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(url['btnPay']))
        driver.find_element_by_id(url['btnPay']).click()
        # 选钱包
        driver.find_element_by_id(url['tvWalletName']).click()
        driver.find_element_by_id(url['ivSelect']).click()

        # 输入密码
        driver.find_element_by_id(url['etPwd']).send_keys(passwd)
        # 按回车
        driver.press_keycode('66')
        WebDriverWait(driver, 120).until(lambda x: x.find_element_by_id(url['tvTip']))
        ele1 = driver.find_element_by_id(url['tvTip'])
        textLast = ele1.text
        self.assertIn('尽快分享哦~',textLast)
       #if textLast == '大红包已生成，尽快分享哦~':
       #    print('发红包成功：', textLast)