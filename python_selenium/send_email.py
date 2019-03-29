# 导入smtplib模块，网络编程的模块,提供了一种很方便的途径发送电子邮件,它对smtp协议进行了简单的封装。
import smtplib,time
# 导入MIMEText库用来做纯文本的邮件模板
from email.mime.text import MIMEText

# 发邮件相关参数
smtpsever = 'smtp.163.com'
sender = 'jarthong@163.com'  # 发送邮件的账号
psw = 'h8262056jx'  # 邮箱客户端授权码（注意不是秘密）
receiver = '652628071@qq.com'  # 接收邮件的账号

# 编辑邮件的内容
subject = '这是一个主题'   # 邮件的主题（可以写项目的自动化测试报告等）
body = str(time.ctime())  # 邮件的正文
msg = MIMEText(body,'html','utf-8')  # 邮件正文的格式
msg['from'] = sender  # 邮件由哪个邮箱来发送
msg['to'] = receiver  # 邮件发给谁
msg['subject'] = subject  # 邮件主题

try:
    smtp = smtplib.SMTP()  # 获取对象
    smtp.connect(smtpsever)  # 链接服务器
    smtp.login(sender,psw)  # 使用账号、授权码登录
    smtp.sendmail(sender,receiver,msg.as_string())  # 发送动作（从sender邮箱发给receiver邮箱，发送内容）
    print('邮件发送成功')
except Exception as message:
    print('发送失败，失败信息：{}'.format(message))


