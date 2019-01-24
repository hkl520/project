from base.base_action import BaseAction
import page


class EmailLoadPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
# 点击我的
    def click_btn_my(self):
        self.click_element(page.emailpage_btn_my)
# 点击登录按钮
    def click_btn_load(self):
        self.click_element(page.emailpage_btn_to_load)
# 点击email登录
    def click_btn_email_load(self):
        self.click_element(page.emailpage_btn_email_load)
# 输入用户
    def input_text_email_user(self,content):
        self.input_edit_content(page.emailpage_text_email_user,content)
# 输入密码
    def input_text_email_password(self,content):
        self.input_edit_content(page.emailpage_text_email_password,content)
# 点击登录
    def click_btn_loading(self):
        self.click_element(page.emailpage_btn_loading)
# 滑动至低端
    def scoll_low_side(self):
        elefrom = self.find_element(page.emailpage_scroll_from)
        eleto = self.find_element(page.emailpage_scroll_to)
        self.scroll_from_ele(elefrom,eleto)
# 点击设置
    def click_text_set(self):
        self.click_element(page.emailpage_btn_set)
# 点击退出
    def click_text_quit(self):
        self.click_element(page.emailpage_text_quit)
        self.click_element(page.emailpage_popup_quit)
