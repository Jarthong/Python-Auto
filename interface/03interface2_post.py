# post请求
'''
1.post请求的基本的例子
2.data json的使用
3.post请求之定制请求头信息
'''
'''
# json参数的使用：json可以自动将字典类型的对象自动转换成json格式，所以可以直接等于一个字典
import requests,json
# 带参数的post请求示例
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", json=payload,timeout=10)

# 返回响应的json编码的内容,r.json()返回的是一个字典
r1 = r.json()
print(type(r1))
print(r1)

# 以文本字符串的形式展示,r.text返回的是一个字符串
r2 = r.text
print(type(r2))
print(r2)

# 进行序列化、格式化 （转换成json字符串）
r1_str = json.dumps(r1, indent=4, sort_keys=True)
print('序列化后的类型是：{} \n序列化后的数据是：\n{} '.format(type(r1_str), r1_str))



# data参数的使用，需要进行序列化后再传入
# import requests,json
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=json.dumps(payload), timeout=10)
r3 = r.json()
print(r3)
print(json.dumps(r3,indent=4))
'''

# post请求之定制请求头信息
import requests,json
import time
import hashlib
url = 'https://www.13322ty.com/api/account/login/login'
data = {'account': '15915773544', 'password': '8a1148a74ba479fcaca5e34f5de73d45'}

# 登录账号
r = requests.post(url=url, data=data,verify=False)
r1 = r.json()

print(json.dumps(r1,indent=4))
print('-'*100)

# 获取登录后的userId、token
userId = r1['data']['userInfo']['userId']
token = r1['data']['userInfo']['token']
print('userId的值是：', userId)
print('token的值是：', token)
print('-'*100)

# 拼接签名Signature字符串
codeStr = userId + token + str(int(time.time() * 1000))
# hashlib.sha1()，哈希算法加密，对签名进行加密
hashobj = hashlib.sha1()
hashobj.update(codeStr.encode('utf-8'))
ha = hashobj.hexdigest()

# 发布资讯的接口
url2 = 'https://www.13322ty.com/api/manage/news/articleSave'

# 定制请求头
headers = {'Accept': 'application/json, text/plain, */*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
           'X-SNS-Timestamp': str(int(time.time() * 1000)),
           'X-SNS-UserId': userId,
           'X-Token': token,
           'X-SNS-Signature': ha,
           'X-SNS-ClientType': '1'
           }
'''
# 定制请求头
headers = {'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/msword, application/vnd.ms-excel, application/vnd.ms-powerpoint, */*',
           'Accept-Language': 'zh-CN',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
           'X-SNS-Timestamp': str(int(time.time() * 1000)),
           'X-SNS-UserId': userId,
           'X-Token': token,
           'X-SNS-Signature': ha,
           'X-SNS-ClientType': '1'
           }
'''
# 请求参数
data2 = {'content': '<p>这是内容--明天的你会感谢今天努力拼搏的自己</p',
         'articleId': '0',
         'publishStatus': '1',
         'labels': '1',
         'cateId': '15',
         'title': '这是标题-我们都是好孩子！',
         'summary': '这是摘要-jarthong'
         }
# 发布资讯
bbs = requests.post(url=url2, data=data2,headers=headers,verify=False)

# print(json.dumps(bbs1))
print(bbs.json())









