

"""
导航类 这个类负责初始化其他几个类的实例
只要获取导航类的实例 就可以获取其他几个类的实例

"""
from page.home_page import HomePage
from page.regist_login_page import RegistLoginPage
from page.login_page import LoginPage
from page.mine_center_page import MineCenter_page
from page.setting_page import SettingPage


class NavigatePage:
    def __init__(self,driver):
        self.driver = driver

    # 获取home_page实例
    def get_home_mine_obj(self):
       return HomePage(self.driver)

    # 获取regist_login实例
    def get_regist_login_obj(self):
        return RegistLoginPage(self.driver)

    # 获取login实例
    def get_login_obj(self):
        return  LoginPage(self.driver)

    # 获取mine_center实例
    def get_mine_center_obj(self):
        return  MineCenter_page(self.driver)

    # 获取setting实例
    def get_setting_obj(self):
        return  SettingPage(self.driver)
