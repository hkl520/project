
from appium import webdriver

# 只要调用这个函数，就获取一个driver
def init_driver(appPackage,appActivity):
    desired_caps = {}
    # server 启动参数增加两个参数配置（输入中文）
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True


    # 设备信息android不区分大小写
    desired_caps['platformName'] = 'Android'

    # 要跟测试手机版本对应
    desired_caps['platformVersion'] = '5.1'

    desired_caps['automationName'] = 'Uiautomator2'

    # 设备名称值Android可以随便写
    desired_caps['deviceName'] = '192.168.56.101:5555'

    # app信息
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

