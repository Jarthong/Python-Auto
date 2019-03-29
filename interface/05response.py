# response响应信息解析
import requests,json
url = 'https://www.13322ty.com/'
r = requests.get(url=url)
print('响应状态码:',r.status_code)
# print('获取响应体内容:',r.content)
# print('获取响应的文本字符串:',r.text)
print('原始请求内容:', r.raw)
print('原始请求地址:', r.url)
# print('获取请求头部信息:',r.headers)
# 获取头部信息里的Date值
print('获取请求头部信息里的日期值:',r.headers['Date'])
print('获取响应信息中的cookie:', r.cookies)

# r.json(),requests中内置的josn解码器,只有response返回为json格式时，用r.json()打印出响应的内容
# print('获取json解码后的数据:',r.json())

print('失败请求（非200响应）抛出异常',r.raise_for_status())