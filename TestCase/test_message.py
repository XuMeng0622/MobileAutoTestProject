import sys, os

sys.path.append(os.getcwd())

import pytest
from Page.message import message
from CommonLib.driver import init_driver
import time

class Test_Send_Message():
    def setup_class(self):
        self.appPackage = 'com.android.messaging'
        self.appActivity = '.ui.conversationlist.ConversationListActivity'
        self.driver = init_driver(self.appPackage, self.appActivity)
        self.msg_obj = message(self.driver)

    @pytest.mark.parametrize('phone_num', ['13910313389'])
    def test_input_phone_num(self, phone_num):
        self.msg_obj.create_new_conversation()
        self.msg_obj.input_recipient_phone(phone_num)

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('msg', ['hello', 'world', '你好!'])
    def test_send_message(self, msg):
        print('test_send_message')
        self.msg_obj.input_message(msg)
        self.msg_obj.send_message()

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir Report', 'test_message.py'])
    # pytest.main(['-s', 'test_message.py'])
