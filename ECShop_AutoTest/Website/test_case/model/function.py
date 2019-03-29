# from selenium import webdriver
import os

def insert_img(driver,filename):
    '''
    # 以下这两行代码获取到的路径格式E:/Python-test/ECShop_AutoTest/Website/test_case
    function_path = os.path.dirname(__file__)  # 获取function.py的绝对路径
    # print(function_path)
    base_dir = os.path.dirname(function_path)  # 获取model（function.py所在目录）的绝对路径
    print(base_dir)
    base_dir = str(base_dir)  # 其实base_dir本身就是字符类型
    # replace()方法把字符串中的"\" 替换成"/"。（如果指定第三个参数max，则替换不超过 max 次）
    base_dir = base_dir.replace('\\','/')  # 第一个"\"表示转义
    print(base_dir)
    '''
    # 以下这行代码获取到的路径格式E:\Python-test\ECShop_AutoTest\Website\test_case\model
    function_path = os.path.abspath('.')
    # 把路径的"\" 替换成"/"，第一个"\"表示转义
    base_dir = function_path.replace('\\','/')
    # 拆分路径，取第一个值
    base = base_dir.split('/test_case')[0]
    # 拼接路径
    file_path = base + '/test_report/screenshot/' + filename
    # 截图
    driver.get_screenshot_as_file(file_path)



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://192.168.133.129/ecshop')
    insert_img(driver,'jarthong.png')
    driver.quit()
