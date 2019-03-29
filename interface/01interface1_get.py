# get请求
import requests
# # 没有参数的get请求
url = 'http://www.baidu.com'
# 发送请求，获取服务器返回的数据
r = requests.get(url=url,timeout=10)
# print(r.text)  # 返回响应的信息
print(r.status_code)
print(r.url)
print(r.cookies)
print(r.is_permanent_redirect)

# 有参数的get请求
url = 'http://www.baidu.com'
payload = {'wd':'pythong'}
r = requests.get(url=url,params=payload)
print(r.url)
print()
# 如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，
# 我们可以通过Response.raise_for_status() 来抛出异常
print(r.raise_for_status())
print(r.headers)
print(r)


