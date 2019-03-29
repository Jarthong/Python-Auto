'''
# 将公共部分封装成一个函数，供其他文件调用
from selenium import webdriver
from module2 import login
dr = webdriver.Chrome()
dr.get('https://mail.163.com/')
login(dr)
# dr.quit()
'''

# 将公共部分封装到类里面
from selenium import webdriver
from module2 import User
from time import sleep

dr = webdriver.Chrome()
dr.get('https://mail.163.com/')

L = User(dr)  # 实例化一个对象
L.login('hong_jun_xiong','h265358979.jx')
sleep(5)
L.logout()
dr.quit()