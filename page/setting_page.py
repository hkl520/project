import allure

from base.base_action import BaseAction
import page

class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
     # 滑动至底部
    @allure.step('滑动至底部')
    def swipe_screen_up(self,num):
        self.swipe_screen(num)

    @allure.step('退出登录')
    def click_btn_quit(self):
        allure.attach('退出登录','点击退出按钮')
        self.click_element(page.setting_btn_quit)
        allure.attach('退出登录','点击确认退出弹框')
        self.click_element(page.setting_btn_sure_quit)
