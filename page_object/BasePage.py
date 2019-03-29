from time import sleep

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

    def find_element(self,*loc):
        return self.driver.find_element(*loc)


