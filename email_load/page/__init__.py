from selenium.webdriver.common.by import By

emailpage_btn_my = (By.XPATH,"//*[contains(@text,'我的') and contains(@resource-id,'id/tv_tab_title')]")

emailpage_btn_to_load = (By.CLASS_NAME,"android.widget.Button")

emailpage_btn_email_load = (By.ID,"io.manong.developerdaily:id/btn_email")

emailpage_text_email_user = (By.ID,"io.manong.developerdaily:id/edt_email")

emailpage_text_email_password = (By.ID,"io.manong.developerdaily:id/edt_password")

emailpage_btn_loading = (By.ID,"io.manong.developerdaily:id/btn_login")

emailpage_scroll_from = (By.XPATH,"//*[contains(@text,'昨日')]")

emailpage_scroll_to = (By.XPATH,"//*[contains(@text,'分享')]")

emailpage_btn_set = (By.XPATH,"//*[contains(@text,'设置')]")

emailpage_text_quit = (By.ID,"io.manong.developerdaily:id/btn_logout")

emailpage_popup_quit = (By.ID,"io.manong.developerdaily:id/md_buttonDefaultPositive")

