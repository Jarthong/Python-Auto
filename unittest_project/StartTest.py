import time,os
import unittest
from common.HTMLTestRunner import HTMLTestRunner
from common.function import new_file, send_email

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件（StartTest.py）路径
    case_path = os.path.join(current_path, 'TestCase')  # 测试用例路径
    report_path = os.path.join(current_path, 'report')  # 测试报告路径
    # 读取某路径下的文件,第二参数是一个文件匹配
    test_list = unittest.defaultTestLoader.discover(case_path, pattern='*_case.py')
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # 定义报告的路径和名称
    file_name = report_path + '\\' + now_time + '_result.html'
    # print(file_name)
    fp = open(file_name, 'wb')  # 'wb'创建（写入）二进制文件
    runner = HTMLTestRunner(stream=fp,  # 读取的是哪个文件
                            title='自动化测试报告',  # 测试报告的主题，可自定义
                            description='测试环境：Win7 Chrome browser 67 version')  # 环境描述，可自定义
    runner.run(test_list)  # 调用HTMLTestRunner()下的run()方法，运行所有的测试用例，并写入相关数据到报告文件fp中
    fp.close()
    new_report = new_file(report_path)  # 调用‘查找最新报告’的方法。（传入报告的路径）
    send_email(new_report)  # 调用‘发送邮件’的方法。（把最新的报告作为参数传入）

