from LoginPage import *
from selenium import webdriver
driver = webdriver.Chrome()
username = 'jarthong1'
password = 'h000001'
test_user_login(driver,username,password)
sleep(5)
driver.quit()