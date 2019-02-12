import allure

from base.base_action import BaseAction
import page

class RegistLoginPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击已有账号')
    def click_text_already_account(self):
        self.click_element(page.regist_login_text_already_account)
        