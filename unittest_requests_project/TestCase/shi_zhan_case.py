import unittest, requests, json
import uuid

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://www.imsam.cn:3000'

    @classmethod
    def tearDownClass(cls):
        pass

    def test01_register(self):
        '''新用户注册'''
        path = '/register'
        payload = {'username': 'jarthong1', 'password': 'h123456', 'password_confirmation': 'h123456'}
        r = requests.post(url=self.url + path, json=payload)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['username'], 'jarthong1')

    def test02_login(self):
        '''登录接口'''
        path = '/login'
        payload = {'username': 'jarthong1', 'password': 'h123456'}
        r = requests.post(url=self.url + path, json=payload)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['username'], 'jarthong1')

    def gettoken(self):
        '''封装登录返回的token'''
        path = '/login'
        payload = {'username': 'jarthong1', 'password': 'h123456'}
        r = requests.post(url=self.url + path, json=payload)
        return r.json()['token']

    def test03_get_all_tasks(self):
        '''获取所有任务接口'''
        # 每个测试用例都是独立的，每个测试用例调用一次gettoken()这个方法，则都会运行一次gettoken（）
        headers = {'Authorization': 'Bearer ' + self.gettoken()}
        path = '/api/tasks'
        r = requests.get(url=self.url + path, headers=headers)
        self.assertEqual(r.status_code, 200)
        # self.assertEqual(r.json()[0]['done'],True) # 返回的第一个任务的done值不一定是True

    def test04_create_taske(self):
        '''创建任务接口'''
        headers = {'Authorization': 'Bearer ' + self.gettoken()}
        path = '/api/tasks'
        # a = str(uuid.uuid4())  # 生成一个随机字符串
        a = 'jarthong11'
        payload = {'title': a, 'desc': '我们都是好孩子！'}
        r = requests.post(url=self.url + path, json=payload, headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['title'],a)

    def getid(self):
        '''封装创建任务返回的id'''
        headers = {'Authorization': 'Bearer ' + self.gettoken()}
        path = '/api/tasks'
        payload = {'title': 'jarthong12', 'desc': '我们都是好孩子！'}
        r = requests.post(url=self.url + path, json=payload, headers=headers)
        return r.json()['id']

    def test04_put_taske(self):
        '''完成任务的接口'''
        headers = {'Authorization': 'Bearer ' + self.gettoken()}
        # 这个测试用例，由于调用了getid（），getid（）方法里的代码才会运行，不然getid（）里的代码不运行
        # 所以这里完成的任务是getid（）方法里所创建的任务，而不是test04_create_taske()用例里创建的任务
        path = '/api/tasks/' + str(self.getid())
        r = requests.put(url=self.url + path, headers=headers)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['done'], True)  # 完成任务后，done的值会变成True

    def test05_delete_taske(self):
        '''删除任务的接口'''
        headers = {'Authorization': 'Bearer ' + self.gettoken()}
        taske_id = str(self.getid())  # 获取一个任务ID，其实是调用get()方法先生成了一个任务
        path = '/api/tasks/' + taske_id
        r = requests.delete(url=self.url + path, headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['id'],taske_id)  # 断言删除的ID号


if __name__ == '__main__':
    unittest.main(verbosity=2)