# 面向对象实现自动化测试脚本封装
from selenium import webdriver
from time import sleep
# 整合进显示等待，故引入By类、显示等待的类、判断元素的类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait_time = 10  # 设置显示等待的总时长

class Jarthong():
    # 类名使用Test报错(Jarthong)

    def __init__(self):
        self.dr = webdriver.Chrome()

    def by_id(self,locator):
        # 显示等待，二次封装。（显示等待也是可以定位元素）
        element = (By.ID,locator)
        return WebDriverWait(self.dr,wait_time,0.5).until(EC.presence_of_element_located(element))

    def by_css(self,locator):
        element = (By.CSS_SELECTOR,locator)
        return WebDriverWait(self.dr,wait_time,0.5).until(EC.presence_of_element_located(element))

    def get_URL(self,url):
        return self.dr.get(url)  # 打开网址

    def input_text(self,locator,text):
        return self.by_id(locator).send_keys(text)  # 找到输入框，输入文本

    def click_btn(self,locator):
        return self.by_css(locator).click()  # 找到点击按钮，点击一下

    def close_windws(self):
        return self.dr.quit()

    def print_title(self):
        print(self.dr.title)  # 打印页面标题

    def assert_text(self,text):
        try:
            sleep(2)
            if text in self.dr.title:
                print('"{}"搜索成功'.format(text))
            else:
                print('没有找到"{}",检查下你实际搜索的是哪个关键字'.format(text))
        except Exception as msg:
            print('报错了!{}'.format(msg))

if __name__ == '__main__':
    L = Jarthong()
    L.get_URL('http://baidu.com')
    L.input_text('kw','jarthong')
    L.click_btn('#su')
    sleep(3)
    L.print_title()
    L.assert_text('jarthong')
    sleep(2)
    L.close_windws()