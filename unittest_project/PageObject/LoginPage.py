from unittest_project.PageObject.BasePage import *
from selenium.webdriver.common.by import By

class LoginPase(Page):
    # 登陆页面模型
    url = '/user.php'
    # 定位器
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME, 'submit')
    logout_loc = (By.LINK_TEXT, '退出')

    # 登录的用户名
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 登录的密码
    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 登录的按钮
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 定义统一登录入口（入参设置默认登录账号）
    def user_login(self, username='jarthong1', password='h000001'):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    # 定义退出登录
    def user_logout(self):
        self.find_element(*self.logout_loc).click()

    user_login_success_loc = (By.CLASS_NAME,'f4_b')
    user_login_error_loc = (By.XPATH,'/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[1]')

    # 登录成功提示
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc).text

    # 账号或者密码错误的提示
    def user_login_error_hint(self):
        return self.find_element(*self.user_login_error_loc).text

    # 账号密码为空的提示
    # def user_password_null(self):
    #     return self.driver.switch_to.alert.text


