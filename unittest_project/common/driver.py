from selenium import webdriver
# 选择运行脚本的浏览器
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    # driver.get('http://192.168.133.129/ecshop')
    return driver

if __name__ == '__main__':
    browser()
