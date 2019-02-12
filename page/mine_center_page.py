import allure

from base.base_action import BaseAction
import page

class MineCenter_page(BaseAction):
    def __init__(self,driver):
       BaseAction.__init__(self,driver)

    @allure.step('个人中心')
    def click_btn_setting(self):
        allure.attach('个人中心','点击设置按钮')
        self.click_element(page.mine_btn_setting)