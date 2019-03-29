from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()

# 自定义元素方法 selenium二次封装
def by_id(locator):
    return dr.find_element_by_id(locator)
def by_css(locator):
    return dr.find_element_by_css_selector(locator)

# 面向过程实现自动化测试脚本运行
def get(url):
    return dr.get(url)
def input_text(locator,text):
    return by_id(locator).send_keys(text)
def click_btn(locator):
    return by_css(locator).click()
def quit_browser():
    return dr.quit()

# 把整个操作过程封装成一个方法
def searc_content(url,locator1,text,locator2):
    get(url)
    input_text(locator1,text)
    click_btn(locator2)
    sleep(3)
    quit_browser()

if __name__ == '__main__':
    # URL = 'https://www.baidu.com'
    # get(URL)
    # input_text('kw','jarthong')
    # click_btn('#su')
    # sleep(3)
    # quit_browser()
    searc_content('https://www.baidu.com','kw','jarthong','#su')  # 直接调用方法
