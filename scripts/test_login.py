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
        tag = login_data.get(i).get('tag')
        except_data = login_data.get(i).get('except_data')
        data_list.append((username,password,tag,except_data))
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

    @pytest.mark.parametrize('username,password,tag,except_data', get_test_login_data())
    def test_login(self,username,password,tag,except_data):

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

        if tag == 1:
            try:
                # 点击我的中心的设置
                self.navigate.get_mine_center_obj().click_btn_setting()

               # 滑动至底部
                self.navigate.get_setting_obj().swipe_screen(1)
               # 点击并确认退出
                self.navigate.get_setting_obj().click_btn_quit()
            except Exception:
                self.navigate.get_login_obj().get_screen()
        else:
            # 获取吐司内容
            toast_mag = self.navigate.get_login_obj().find_element(page.toast_pwd_error).text
            #  判断预期结果与实际结果一致    断言失败会执行逗号后边的代码
            assert toast_mag == except_data,self.navigate.get_login_obj().get_screen()
             # 关闭当前页面
            self.navigate.get_login_obj().click_element(page.login_btn_close_loginpage)


