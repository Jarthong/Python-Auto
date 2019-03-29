import os, time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 发送附件的方法
from email.header import Header

def insert_img(driver,filename):
    # 以下这行代码获取到的路径格式E:\Python-test\unittest_project\common (realpath也可以写成dirname)
    function_path = os.path.dirname(os.path.realpath(__file__))
    # function_path = os.path.abspath('.')  在其他模块调用该模块的时候，获取的路径是其他模块的绝对路径
    # 把路径的"\" 替换成"/"(window中也可以省)，第一个"\"表示转义
    base_dir = function_path.replace('\\','/')
    # 拆分路径，取第一个值
    base = base_dir.split('/common')[0]
    # 拼接路径
    file_path = base + '/screenshot/'
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # 给截图名称前加上当前时间
    file_name = file_path + now_time + filename + '.png'
    # 截图
    driver.get_screenshot_as_file(file_name)

# 查找最新的报告
def new_file(path):
    lists = os.listdir(path)  # 列出path目录下面的所有文件和目录，以列表的形式存在
    lists.sort()  # 从小到大排序
    # 列表生成式，从lists中遍历取值赋值给第一个x，且加上条件判断，x以“.html”结尾。生成的还是一个列表
    file = [x for x in lists if x.endswith('.html')]
    new_file_path = os.path.join(path,file[-1])  # 取出最后一个文件名与path（报告）路径拼接，即最新的报告
    return new_file_path

def send_email(file):
    f = open(file,'rb')
    mail_body = f.read()
    f.close()
    # 发邮件相关参数
    smtpsever = 'smtp.163.com'  # 邮箱的SMTP服务器地址
    sender = 'jarthong@163.com'  # 发送邮件的账号
    password = 'h8262056jx'  # 邮箱客户端授权码（注意不是秘密）
    receiver = 'jarthong@163.com'  # 接收邮件的账号
    now_date = time.strftime('%Y-%m-%d')
    email_name = '自动化测试报告' + now_date  # 邮件主题的名称，可自定义
    att_name = 'test_report' + now_date + '.html'  # 邮件的附件报告名称，可自定义
    # 定义邮件
    msg = MIMEMultipart()  # 实例化一个邮件对象
    msg['subject'] = Header(email_name,'utf-8')  # 设置邮件主题
    msg['from'] = sender  # 定义发送人邮箱
    msg['to'] = receiver  # 定义收件人邮箱
    # 添加邮件正文
    body = MIMEText(mail_body,'html','utf-8')
    msg.attach(body)
    # 添加邮件附件
    att = MIMEText(mail_body,'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename='+att_name
    msg.attach(att)

    # 连接邮箱服务器发送邮件
    try:
        smtp = smtplib.SMTP()  # 获取（实例化）对象
        smtp.connect(smtpsever)  # 链接服务器
        smtp.login(msg['from'], password)  # 使用账号、授权码登录
        smtp.sendmail(msg['from'], msg['to'], msg.as_string())  # 发送动作（从sender邮箱发给receiver邮箱，发送内容）
        print('邮件发送成功')
    except Exception as message:
        print('发送失败，失败信息：{}'.format(message))



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.133.129/ecshop')
    insert_img(driver,'jarthong')
    driver.quit()
