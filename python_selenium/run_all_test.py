from common.HTMLTestRunner import HTMLTestRunner
import unittest,time,os

# 获取当前文件（run_all_test.py）路径
current_path = os.path.dirname(os.path.realpath(__file__))
# 测试用例路径
case_path = os.path.join(current_path,'test_case')
# 测试报告路径
report_path = os.path.join(current_path,'report')
# 读取某路径下的文件,第二参数是一个文件匹配
test_list = unittest.defaultTestLoader.discover(case_path,pattern='*_case.py')

if __name__ == '__main__':
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # 定义报告的路径和名称
    file_name = report_path + '\\' + now_time + '_result.html'
    print(file_name)
    fp = open(file_name,'wb')  # 'wb'创建（写入）二进制文件
    runner = HTMLTestRunner(stream=fp,  # 读取的是哪个文件
                            title='ECShop测试项目',  # 测试报告的主题，可自定义
                            description='Win7 Chrome browser 67 version')  # 环境描述，可自定义
    runner.run(test_list)  # 运行所有的测试用例
    fp.close()






