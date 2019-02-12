"""
类里面包含公共操作：查找元素，点击元素，向输入框输入内容
"""
import time

import allure


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 这个方法是自己定义的查找元素的方法，loc是元组
    def find_element(self, loc):
        time.sleep(2)
        return self.driver.find_element(loc[0], loc[1])

    def find_elements(self, loc):
        time.sleep(2)
        return self.driver.find_elements(loc[0], loc[1])

    # 点击元素的方法
    def click_element(self, loc):
        time.sleep(2)
        self.find_element(loc).click()

    # 输入内容
    def input_edit_content(self, loc, content):
        time.sleep(2)
        input_element = self.find_element(loc)
        input_element.clear()
        input_element.send_keys(content)

    # 模糊滑动

    def scroll_from_ele(self, ele1, ele2):
        time.sleep(2)
        return self.driver.scroll(ele1, ele2)

    def swipe_screen(self, tag):
        time.sleep(2)
        screen_size = self.driver.get_window_size()
        width = screen_size.get('width')
        height = screen_size.get('height')

        if tag == 1:  # 向上滑动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向下滚动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滚动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滚动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    def get_screen(self):
        # 截图名字
        # pang_name = './screen/{}'.format(int(time.time()))
        png_name = './screen/{}.png'.format(time.strftime('%Y%m%d%H%M%S'))
        # 截图
        self.driver.get_screenshot_as_file(png_name)

         # rb 以二进制的方式读取数据
         # 把截图信息放到报告里
        with open('png_name','rb') as f:
            allure.attach('截图名字',f.read(),allure.attach_type.png)
