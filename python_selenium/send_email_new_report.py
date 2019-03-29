import smtplib
from email.mime.text import MIMEText
from common.HTMLTestRunner import HTMLTestRunner
import time,os
import unittest
from email.mime.multipart import MIMEMultipart  # 发送附件的方法
from email.header import Header
# from email import encoders
# from email.mime.base import MIMEBase

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

    # # 添加附件 尝试一下其他方法
    # with open(file,'rb') as f:
    #     mime = MIMEBase('base','html',filename=att_name)  # 设置附件的MIME和文件名，这里是png类型:
    #     mime.add_header('Content-Disposition', 'attachment', filename=att_name)  # 加上必要的头信息:
    #     mime.add_header('Content-ID', '<0>')  # 加上必要的头信息:
    #     mime.add_header('X-Attachment-Id', '0')  # 加上必要的头信息:
    #     mime.set_payload(f.read())  # 把附件的内容读进来:
    #     encoders.encode_base64(mime)  # 用Base64编码:
    #     msg.attach(mime)  # 添加到MIMEMultipart:

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
    current_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件（run_all_test.py）路径
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
    runner.run(test_list)  # 运行所有的测试用例
    fp.close()
    new_report = new_file(report_path)  # 调用‘查找最新报告’的方法。（传入报告的路径）
    send_email(new_report)  # 调用‘发送邮件’的方法。（把最新的报告作为参数传入）

