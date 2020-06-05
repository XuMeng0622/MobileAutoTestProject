from selenium.webdriver.common.by import By

'''
发送短信模块
'''
# 新建会按钮
new_conversation_button = (By.ID, 'com.android.messaging:id/start_new_conversation_button')
# 接收人号码输入框
recipient_box = (By.ID, 'com.android.messaging:id/recipient_text_view')
# 消息输入框
msg_box = (By.CLASS_NAME, 'android.widget.EditText')
# 发送框
send_button = (By.ID, 'com.android.messaging:id/self_send_icon')