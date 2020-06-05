from selenium.webdriver.support.wait import WebDriverWait


class base():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, ele):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*ele))

    def click(self, ele):
        print(*ele)
        self.find_element(ele).click()

    def input_keyword(self, ele, keyword):
        self.find_element(ele).send_keys(keyword)