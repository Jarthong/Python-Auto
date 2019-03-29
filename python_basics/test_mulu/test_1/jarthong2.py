import os,time

def insert_img(driver,filename):
    # 以下这行代码获取到的路径格式E:\Python-Auto\python_basics\test_mulu2
    function_path = os.path.abspath('.')
    print(function_path)
    # 把路径的"\" 替换成"/"(window中也可以省)，第一个"\"表示转义
    base_dir = function_path.replace('\\','/')
    print(base_dir)
    # # 拆分路径，取第一个值
    # base = base_dir.split('/common')[0]
    # 拼接路径
    file_path = base_dir + '/' + filename
    print(file_path)
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # 给截图名称加上当前时间
    file_name = file_path + now_time + '.png'
    print(file_name)
    # 截图
    driver.get_screenshot_as_file(file_name)