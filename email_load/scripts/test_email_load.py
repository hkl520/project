import os,sys
sys.path.append(os.getcwd())
import time

from base.init_driver import init_driver
from page.email_load_page import EmailLoadPage


class TestEmailLoad():

    def setup_class(self):
        # 初始化driver
        self.driver = init_driver('io.manong.developerdaily','io.toutiao.android.ui.activity.MainActivity')
        # 初始化EmailLoadPage
        self.emailloadpage =EmailLoadPage(self.driver)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()


    def test_email_load(self):
        # 点击我的
         self.emailloadpage.click_btn_my()

        # 点击登录按钮
         self.emailloadpage.click_btn_load()

        # 点击email登录
         self.emailloadpage.click_btn_email_load()

        # 输入用户
         self.emailloadpage.input_text_email_user("benbenxiong567@163.com")

        # 输入密码
         self.emailloadpage.input_text_email_password('139432500')

        # 点击登录
         self.emailloadpage.click_btn_loading()

        # 滑动至低端
         self.emailloadpage.scoll_low_side()

        # 点击设置
         self.emailloadpage.click_text_set()

        # 点击退出
         self.emailloadpage.click_text_quit()