from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC   # 判断元素是否出现的类
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待需要结合WebDriverWait这个类使用
from selenium.webdriver.common.by import By  # 元素定位的另外一种写法

class Page(object):
    # 页面基础类，用于所有页面的继承
    def __init__(self,driver):
        self.driver = driver
        self.base_url = 'http://192.168.133.129/ecshop'
        self.timeout = 10

    def _open(self,url):
        url2 = self.base_url + url
        print('测试页面的网址是 %s' %url2)
        self.driver.maximize_window()
        self.driver.get(url2)
        sleep(2)
        assert self.driver.current_url == url2,'没有登陆到这个网址：%s' %url2

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # def find_element(self, *loc):
    #     return WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(*loc))

    # 获取警告框文本信息
    def switch_alert_text(self):
        return self.driver.switch_to.alert.text

    # 接受警告框（点击确定）
    def switch_alert_accept(self):
        return self.driver.switch_to.alert.accept()

    # 解散警告框（点击取消）
    def switch_alert_dismiss(self):
        return self.driver.switch_to.alert.dismiss()


