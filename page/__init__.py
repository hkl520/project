from selenium.webdriver.common.by import By

# 应用包名和启动名
appPackage = 'com.yunmall.lc'
appActivity = 'com.yunmall.ymctoc.ui.activity.MainActivity'

# home页面
# 点击我的
home_btn_mine = (By.ID,"com.yunmall.lc:id/tab_me")

# 登录注册页面
# 定位到已有账户登录
regist_login_text_already_account= (By.ID,"com.yunmall.lc:id/textView1")


# 登录页面
login_input_account_username= (By.ID,"com.yunmall.lc:id/logon_account_textview")
login_input_account_password= (By.ID,"com.yunmall.lc:id/logon_password_textview")
login_btn_account_loading = (By.ID,"com.yunmall.lc:id/logon_button")
toast_pwd_error = (By.XPATH,"//*[contains(@text,'密码错误')]")
login_btn_close_loginpage=(By.ID,'com.yunmall.lc:id/ymtitlebar_left_btn_image')


# 我的页面
# 点击设置，进入设置
mine_btn_setting= (By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")

# 设置页面
# 退出
setting_btn_quit = (By.ID,"com.yunmall.lc:id/setting_logout")
# 确认退出
setting_btn_sure_quit = (By.ID,"com.yunmall.lc:id/ymdialog_right_button")
