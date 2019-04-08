from appium import webdriver
import time
from common import  read_execl
url=read_execl.read_excel('./test_data/element.xlsx')
print(url['platformName'],url['platformVersion'],url['deviceName'],url['appActivity'],url['appium_url'])
def login():

    desired_capabilities = {
        'platformName': url['platformName'],
        "platformVersion": url['platformVersion'],
        "deviceName": url['deviceName'],
        "appPackage": url['appPackage'],
        "appActivity": url['appActivity'],
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "noReset": True,
        "automationName": "uiautomator2"
    }

    driver = webdriver.Remote(
        command_executor=url['appium_url'],
        desired_capabilities=desired_capabilities
    )
    driver.implicitly_wait(10)
    time.sleep(4)
    try:
        driver.find_element_by_id(url['btnCancel']).click()
    except:
        pass
    try:
        driver.find_element_by_id(url['btnCancel']).click()
    except:
        pass

    return  driver