import unittest,random
from unittest_project.common import function,myunit
from unittest_project.PageObject.LoginPage import *

class LoginTest(myunit.StartEnd):

    def test1_login_normal(self):
        """输入正确的账号和密码"""
        po = LoginPase(self.driver)
        username = 'jarthong1'
        password = 'h000001'
        po.user_login(username, password)
        self.assertIn(po.user_login_success_hint(), username)
        function.insert_img(self.driver, '正确的用户名和密码')
        po.user_logout()

    def test2_login_user_pwd_null(self):
        """用户名和密码为空"""
        po = LoginPase(self.driver)
        po.user_login('', '')
        self.assertIn('用户名不能为空', po.switch_alert_text())
        po.switch_alert_accept()
        function.insert_img(self.driver, '用户名和密码为空')

    def test3_login_user_null(self):
        """用户名为空"""
        po = LoginPase(self.driver)
        po.user_login('', 'h000001')
        self.assertIn('用户名不能为空', po.switch_alert_text())
        po.switch_alert_accept()
        function.insert_img(self.driver, '用户名为空')

    def test4_login_password_null(self):
        """密码为空"""
        po = LoginPase(self.driver)
        po.user_login('jarthong1', '')
        self.assertIn('密码不能为空', po.switch_alert_text())
        po.switch_alert_accept()
        function.insert_img(self.driver, '密码为空')

    def test5_login_user_error(self):
        """用户名与密码不匹配"""
        po = LoginPase(self.driver)
        m = random.choice('abcdefghijklmmopqrstuvwxyz')
        username = 'jarthong' + m
        password = '123456'
        po.user_login(username, password)
        function.insert_img(self.driver, '用户名与密码不匹配')
        self.assertIn('用户名', po.user_login_error_hint())



if __name__ == '__main__':
    unittest.main()

