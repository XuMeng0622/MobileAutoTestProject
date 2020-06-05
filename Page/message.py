from selenium.webdriver.common.by import By
from CommonLib.base import base
import Page


class message(base):
    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = driver

    #新建会话
    def create_new_conversation(self):
        self.click(Page.new_conversation_button)

    #输入接收人的手机号
    def input_recipient_phone(self, phone_num):
        self.input_keyword(Page.recipient_box, phone_num)
        self.driver.keyevent(66)  # KEYCODE_ENTER 回车键66

    #输入消息并发送消息
    def input_message(self, msg):
        self.input_keyword(Page.msg_box, msg)

    #发送消息
    def send_message(self):
        self.click(Page.send_button)





