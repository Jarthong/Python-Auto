import unittest
from unittest_project.common.driver import *
from selenium.webdriver.support.ui import WebDriverWait

# 单元测试框架
class StartEnd(unittest.TestCase):
    # 只执行一次的前置条件
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # 只执行一次的后置条件
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
