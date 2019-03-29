import requests, json

url = 'http://www.imsam.cn:3000'

# 新用户注册
path = '/register'
payload = {'username':'jarthong1', 'password':'h123456', 'password_confirmation':'h123456'}
r = requests.post(url=url+path,json=payload)
print('新用户注册返回的json：\n', r.json())
print('-'*100)

# 登录接口
path = '/login'
payload = {'username':'jarthong1', 'password':'h123456'}
r = requests.post(url=url+path,json=payload)
print('登录接口返回的json：\n', r.json())
token = r.json()['token']
print('获取到的token值为：\n', token)
print('-'*100)

# Http头部信息（含登录后的token）
headers = {'Authorization':'Bearer '+token}

# 获取所有任务接口
path = '/api/tasks'
r = requests.get(url=url+path, headers=headers)
print('获取所有任务接口返回的json：\n', r.json())
print('-'*100)

# 创建任务接口
path = '/api/tasks'
payload = {'title':'这是一个标题', 'desc':'我们都是好孩子！'}
r = requests.post(url=url+path, json=payload, headers=headers)
print('创建任务接口返回的json：\n', r.json())
# 获取创建任务后的任务ID号
task_id = r.json()['id']
print('-'*100)

# 完成任务接口
path = '/api/tasks/'+str(task_id)
r = requests.put(url=url+path, headers=headers)
print('完成任务接口返回的json:\n', r.json())
print('-'*100)

# 删除任务接口
path = '/api/tasks/'+str(task_id)
r = requests.delete(url=url+path, headers=headers)
print('删除任务接口返回的json:\n', r.json())