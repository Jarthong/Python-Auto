from selenium import webdriver

from python_basics.test_mulu.test_1.jarthong2 import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.133.129/ecshop')
insert_img(driver,'jarthong')
driver.quit()