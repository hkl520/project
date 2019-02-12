import allure

from base.base_action import BaseAction
import  page
class LoginPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
     #输入用户
    @allure.step('输入用户名')
    def input_already_usename(self,content):
        self.input_edit_content(page.login_input_account_username,content)

    # 输入密码
    @allure.step('输入密码')
    def input_already_password(self,content):
        self.input_edit_content(page.login_input_account_password,content)

    # 点击登录
    @allure.step('点击登录')
    def click_btn_loading(self):
        self.click_element(page.login_btn_account_loading)

    # 点击关闭登录页面
    @allure.step('关闭登录页面')
    def click_close_loginpage(self):
        self.click_element(page.login_btn_close_loginpage)