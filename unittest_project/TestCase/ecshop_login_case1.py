# 单元测试
import unittest
from selenium import webdriver

class ecshop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Chrome()
        cls.url = 'http://192.168.133.129/ecshop/user.php'

    @classmethod
    def tearDownClass(cls):
        cls.d.quit()

    # 登陆成功
    def test0_login_success(self):  # test0里的“0”，让测试用例按顺序执行，不然就按用例名字依次执行
        '''用户名和密码正确'''  # 每个用例下的第一行可以这样注释，在生成的报告的用例名称中会显示
        d = self.d  # 这里可以直接把上面的self.d赋值给d,也可以像下面那样直接用。
        d.get(self.url)
        d.find_element_by_name("username").send_keys("jarthong1")
        d.find_element_by_name("password").send_keys("h000001")
        d.find_element_by_class_name("us_Submit").click()
        self.assertIn('jarthong', d.find_element_by_class_name("f4_b").text)
        # 截屏图片保存路径使用相对路径，可移植性。单纯该脚本运行的时候，是上级文件下的img,“../img”，
        # 使用上级文件下的“run_all_test.py”脚本运行时，使用的是运行脚本的当前路径下的img文件夹,即“./img”
        d.get_screenshot_as_file("./screenshot/login_success.png")
        # print("测试通过：用户名和密码正确登陆成功")
        d.find_element_by_css_selector("#ECS_MEMBERZONE > font > a:nth-child(3)").click()

    # 用户名错误
    def test1_user_errer(self):
        '''用户名错误登陆失败'''
        d = self.d  # 这里可以直接把上面的self.d赋值给d,也可以像下面那样直接用。
        d.get(self.url)
        d.find_element_by_name("username").send_keys("df")
        d.find_element_by_name("password").send_keys("h000001")
        d.find_element_by_class_name("us_Submit").click()
        self.assertIn('用户名或密码错误', self.d.find_element_by_css_selector('.boxCenterList').text)
        d.get_screenshot_as_file("./screenshot/user_errer.png")
        # print("测试通过：用户名错误登陆失败")

    # 密码错误
    def test2_password_errer(self):
        '''密码错误登陆失败'''
        d = self.d
        d.get(self.url)
        d.find_element_by_name("username").send_keys("jarthong1")
        d.find_element_by_name("password").send_keys("111")
        d.find_element_by_class_name("us_Submit").click()
        self.assertIn('用户名或密码错误', d.find_element_by_css_selector('.boxCenterList').text)
        d.get_screenshot_as_file("./screenshot/password_errer.png")
        # print("测试通过：密码错误登陆失败")

    # 用户名和密码为空
    def test3_login_null(self):
        '''用户名和密码为空登陆失败'''
        d = self.d
        d.get(self.url)
        d.find_element_by_name("username").send_keys("")
        d.find_element_by_name("password").send_keys("")
        d.find_element_by_class_name("us_Submit").click()
        self.assertIn('用户名不能为空', d.switch_to.alert.text)
        d.switch_to.alert.accept()
        d.get_screenshot_as_file("./screenshot/login_null.png")
        # print("测试通过：用户名和密码为空登陆失败")


if __name__ == '__main__':
    unittest.main()





