from appium import webdriver


def init_driver(appPackage, appActivity):
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = '192.168.115.107:5555'
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    desired_caps['unicodeKeyBoard'] = True
    desired_caps['reesetKeyBoard'] = True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

if __name__ == '__main__':
    pass
