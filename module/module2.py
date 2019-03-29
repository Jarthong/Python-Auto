'''
# 将公共部分封装成一个函数，供其他文件调用
from time import sleep
def login(dr):
    sleep(3)
    dr.switch_to.frame('x-URS-iframe')
    dr.find_element_by_name('email').clear()
    dr.find_element_by_name('email').send_keys('hong_jun_xiong')
    dr.find_element_by_name('password').send_keys('h265358979.jx')
    dr.find_element_by_id('dologin').click()
    dr.switch_to.default_content()
    sleep(3)
    dr.find_element_by_class_name('nui-tree-item-text').click()
    sleep(2)
'''


# 将公共部分封装到类里面
from time import sleep
class User():
    def __init__(self,dr):
        self.dr = dr

    def login(self,username,password):
        dr = self.dr
        sleep(3)
        dr.switch_to.frame('x-URS-iframe')
        dr.find_element_by_name('email').clear()
        dr.find_element_by_name('email').send_keys(username)  # 用户设置成变量
        dr.find_element_by_name('password').send_keys(password)  # 密码设置成变量
        dr.find_element_by_id('dologin').click()
        dr.switch_to.default_content()
        sleep(3)
        dr.find_element_by_class_name('nui-tree-item-text').click()
        sleep(2)

    def logout(self):
        dr = self.dr
        dr.find_element_by_css_selector('#_mail_component_39_39 > a').click()
