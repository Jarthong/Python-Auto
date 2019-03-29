
'''
import requests
import time
import hashlib


base_url = 'http://caigou.sippe.ac.cn'

url2 = '/login_supplier_productlist.html'

# 定制请求头
headers1 = {'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
           # 'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN',
           # 'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
           # 'X-SNS-Timestamp': str(int(time.time() * 1000)),
           # 'X-SNS-UserId': userId,
           # 'X-Token': token,
           # 'X-SNS-Signature': ha,
           # 'X-SNS-ClientType': '1'
           }



# 请求参数
data2 = {'txt_username': 'joshua@teempole.com',
         'txt_password': 'ily516400',
         'submit1': 'login',
         }
# 请求
response = requests.post(url=base_url + url2, data=data2, headers=headers, verify=False)
# r.enconding = "utf-8'
# print(r.json())
# print(r.url)
# print(r.raise_for_status())
# print(r.headers)
# print(r)
# print('原始请求内容:', r.raw)

print(response.text)  # 一长串东西...中文编码乱
# print(response.cookies)<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(response.content)  # 一长串东西...中文编码为（ascii编码），
print(response.content.decode("utf-8"))  # 一长串东西...中文正常显示（utf-8编码）
'''

from bs4 import BeautifulSoup
import requests
import datetime

headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Cookie': 'PHPSESSID=qr7vu3vt2e4jguscu04hb7j7s5',
           'Host': 'caigou.sippe.ac.cn',
           'Origin': 'http://caigou.sippe.ac.cn',
           'Referer': 'http://caigou.sippe.ac.cn/index.html',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 Form Data view source view URL encoded'}

# url = "http://caigou.sippe.ac.cn/login_supplier_productlist/517_1.html?name=&number=&brand=&model="
url = "http://caigou.sippe.ac.cn/login_supplier_productlist/517_1.html"

a = 0

login_url = 'http://caigou.sippe.ac.cn/index.html'
login_data = {'txt_username': 'joshua@teempole.com', 'txt_password': 'ily516400', 'submit1': 'login'}
r1 = requests.post(url=login_url, data=login_data, headers=headers)
print('登录接口反应时间：', r1.elapsed.total_seconds())

# print(r1.headers)  # 获得响应头信息
# # print(r.cookies)
# print(r1.text)  # 返回响应的信息

r = requests.get(url=url, headers=headers)
# print(r.text)
print('获取页面信息接口反应时间：', r.elapsed.total_seconds())

soup = BeautifulSoup(r.text, "html.parser")
# button = soup.find_all('button')
# print(button)
# print('-'*100)
numbers = soup.findAll('button', attrs={'name': 'submit3'})
# print(numbers)

# num = numbers[0].get('value')
# print(num)

all_numbers = []

for i in numbers:
#     number = i.get('value')
#     all_numbers.append(number)
# # print('所有的编码：', all_numbers)

    payload = {'txt_category': '', 'txt_name': '', 'txt_number': '', 'txt_brand': '', 'txt_model': '',
               'txt_remark': '', 'submit3': number, 'slt_operator': '*', 'txt_percent': ''}
    r = requests.post(url=url, data=payload, headers=headers)
    print('删除接口反应时间：', r.elapsed.total_seconds())
    print('请求头：', r.headers)
    print('_'*100)
    print(r.text)









'''  
def login():
    login_url = 'http://caigou.sippe.ac.cn/index.html'
    login_data = {'txt_username': 'joshua@teempole.com', 'txt_password': 'ily516400', 'submit1': 'login'}
    r = requests.post(url=login_url, data=login_data, headers=headers)
    print(r)


def del_data():
    while a < 250:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        numbers = soup.findAll('button', {'name': 'submit3'})
        all_numbers = []
        StartTime = datetime.datetime.now()
        for i in numbers:
            all_numbers = i.get('value')
            payload = {'txt_category': '', 'txt_name': '', 'txt_number': '', 'txt_brand': '', 'txt_model': '',
                       'txt_remark': '', 'submit3': all_numbers, 'slt_operator': '*', 'txt_percent': ''}
            requests.post(url=url, data=payload, headers=headers)
            EndTime = datetime.datetime.now()
            Result = (EndTime - StartTime).seconds
            StartTime = EndTime
            print(Result)

if __name__ == '__main__':
'''