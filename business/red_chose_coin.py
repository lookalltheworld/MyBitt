import time


def red_chose_coin(driver,url,coinType,coin):
    driver.find_element_by_id(url['trSelectToken']).click()
    time.sleep(2)
    # 选ETH(Test)

    driver.find_element_by_xpath(url['type_ETH']).click()
    time.sleep(1)
    driver.find_element_by_xpath(url['type_BTC(Test)']).click()
    time.sleep(1)
    driver.find_element_by_xpath(url['type_ETH(Test)']).click()
    time.sleep(1)
    driver.find_element_by_xpath(url['type_VNS']).click()
    time.sleep(1)
    driver.find_element_by_xpath( url['type_BCH(Test)']).click()
    ele_click = url['type'].format(coinType)
    driver.find_element_by_xpath(ele_click).click()
    i = 0
    while i < 10:
        i = i + 1
        try:
            ele_c=url['coin'].format(coin)
            driver.find_element_by_xpath(ele_c).click()

            break
        except:
            try:
               driver.swipe(0.5, 0.9, 0.5, 0.2, 1000)
            except:
                pass
            pass