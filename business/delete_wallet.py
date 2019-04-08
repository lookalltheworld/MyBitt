import time
from selenium.webdriver.support.ui import WebDriverWait
def delete_wallet(driver,url,nan,passwd):
    try:
        driver.find_element_by_id(url['btnCancel']).click()
    except:
        pass
    try:
        driver.find_element_by_id(url['btnCancel']).click()
    except:
        pass
        # 管理
        driver.find_element_by_id(url['manage']).click()
        # 钱包管理
        driver.find_element_by_xpath(url['wallet_manage']).click()
        # 点击1111钱包
        try:
            driver.find_element_by_xpath(nan).click()
        except:
            try:
                driver.swipe(0.5, 0.9, 0.5, 0.2, 1000)
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

        # 删除钱包1

        time.sleep(3)
        driver.find_element_by_id(url['btnDelete']).click()
        time.sleep(1)
        # 确定
        driver.find_element_by_id(url['btnSure']).click()