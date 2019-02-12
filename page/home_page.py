import allure

from base.base_action import BaseAction
import page

class HomePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击我的')
    def click_btn_mine(self):
        allure.attach('点击我的','首页中的我的')
        self.click_element(page.home_btn_mine)