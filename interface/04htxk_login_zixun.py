# post请求之定制请求头信息
import requests
import time
import hashlib
url = 'https://www.13322ty.com/api/account/login/login'
data = {'account': '15915773544', 'password': '8a1148a74ba479fcaca5e34f5de73d45'}

# 登录账号
r = requests.post(url=url, data=data,verify=False)
r1 = r.json()

# 获取登录后的userId、token
userId = r1['data']['userInfo']['userId']
token = r1['data']['userInfo']['token']

# 拼接签名Signature字符串,求苗网站的签名有以下部分组成
codeStr = userId + token + str(int(time.time() * 1000))
# hashlib.sha1()，哈希算法加密，对签名进行加密
hashobj = hashlib.sha1()  # 实例化
hashobj.update(codeStr.encode('utf-8'))  # 指定字符编码，并传入加密
ha = hashobj.hexdigest()  # 返回摘要，作为十六进制数据字符串值

# 发布资讯的接口
url2 = 'https://www.13322ty.com/api/manage/news/articleSave'

# 定制请求头
headers = {'Accept': 'application/json, text/plain, */*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',  # 上面是换行符
           'X-SNS-Timestamp': str(int(time.time() * 1000)),
           'X-SNS-UserId': userId,
           'X-Token': token,
           'X-SNS-Signature': ha,
           'X-SNS-ClientType': '1'
           }
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
bbs = requests.post(url=url2, data=data2, headers=headers, verify=False)
print(bbs.json())  # 打印的内容：{'result': '0', 'msg': '成功', 'data': 93412}



