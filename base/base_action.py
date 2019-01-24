"""
类里面包含公共操作：查找元素，点击元素，向输入框输入内容
"""
import time

class BaseAction:
    def __init__(self,driver):
        self.driver = driver

# 这个方法是自己定义的查找元素的方法，loc是元组
    def find_element(self, loc):
       time.sleep(2)
       return self.driver.find_element(loc[0], loc[1])

    def find_elements(self,loc):
       time.sleep(2)
       return self.driver.find_elements(loc[0], loc[1])
# 点击元素的方法
    def click_element(self,loc):
        self.find_element(loc).click()

# 输入内容
    def input_edit_content(self,loc,content):
       input_element= self.find_element(loc)
       input_element.clear()
       input_element.send_keys(content)

# 模糊滑动

    def scroll_from_ele(self,ele1,ele2):
        time.sleep(2)
        return self.driver.scroll(ele1,ele2)