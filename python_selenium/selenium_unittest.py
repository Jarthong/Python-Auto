''''
# unittest框架用法，每执行一条测试用例，都初始化和数据恢复
import unittest
class Jarthog(unittest.TestCase):
    def setUp(self):
        print('------用例执行前初始化一下------')

    def tearDown(self):
        print('------用例执行后还原一下------\n')

    def test1(self):
        print('执行第一个测试用例！！！')

    def test2(self):
        print('执行第二个测试用例！！！')

    def test3(self):
        print('执行第三个测试用例！！！')

if __name__ == '__main__':
    unittest.main()



# 断言第三个参数的用法
import unittest
class Jarthog(unittest.TestCase):

    def test1(self):
        a = 10
        # assertEqual(a,b，[msg='测试失败时打印的信息']),第三个参数的用法如下：
        self.assertEqual(a,1,'a不等于10，断言失败，这个测试用例不通过')

    def test2(self):
        print('执行第二个测试用例！！！')

if __name__ == '__main__':
    unittest.main()
'''

# setUpClass 和 tearDownClass用法，用于只进行一次初始化动作和一次结束关闭浏览器动作
import unittest
class Jarthong(unittest.TestCase):
    # 只执行一次的前置条件
    @classmethod
    def setUpClass(cls):
        print('------用例执行前初始化一下------')

    # 只执行一次的后置条件
    @classmethod
    def tearDownClass(cls):
        print('------用例执行后还原一下------')

    def test1(self):
        print('执行第一个测试用例！！！')

    def test2(self):
        print('执行第二个测试用例！！！')

    def test3(self):
        print('执行第三个测试用例！！！')

if __name__ == '__main__':
    unittest.main()
