import os,sys
sys.path.append(os.getcwd())
import pytest


import time
from base.init_driver import init_driver
from page.navigate_page import NavigatePage
from base.read_yaml import read_yaml_data
import page



def get_test_login_data():
    data_list = []
    login_data = read_yaml_data('login_already_account.yaml')
    for i in login_data.keys():
        username = login_data.get(i).get('username')
        password = login_data.get(i).get('password')
        data_list.append((username,password))
    return data_list

class TestLogin:
    def setup_class(self):
        # 初始化driver
        self.driver = init_driver(page.appPackage,page.appActivity)
        # 初始化navigate类
        self.navigate = NavigatePage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize('username,password', get_test_login_data())
    def test_login(self,username,password):
       # 点击我的
        time.sleep(3)
        self.navigate.get_home_mine_obj().click_btn_mine()
       # 点击已有账户登录
        time.sleep(3)
        self.navigate.get_regist_login_obj().click_text_already_account()

       # 输入用户

        self.navigate.get_login_obj().input_already_usename(username)
        time.sleep(2)
       # 输入密码
        self.navigate.get_login_obj().input_already_password(password)

        # 点击登录
        self.navigate.get_login_obj().click_btn_loading()

        # 获取吐司内容
        toast_mag = self.navigate.get_login_obj().find_element(page.toast_pwd_error).text
        print(toast_mag)
