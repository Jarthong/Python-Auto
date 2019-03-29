'''
查询城市编码 - API地址 - -

地址: url = 'http://183.62.167.17:10158/CyzgMobileConfigService/GetDataInfo'
请求方法: POST
请求头信息: {'Content-Type': 'application/json;charset=UTF-8'}
请求参数: {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646', "TransferData": "{\'CityId\':430100}"}

import requests, json

url = 'http://183.62.167.17:10158'
path = '/CyzgMobileConfigService/GetDataInfo'
headers = {'Content-Type': 'application/json;charset=UTF-8'}
payload = {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646',
           "TransferData": "{\'CityId\':430100}"}

r = requests.post(url=url + path, json=payload, headers=headers)
print(r.json())
# print(r.text)
# print(json.dumps(r.json(), indent=4, ensure_ascii=False))

# 接口测试的断言：必须同时包含以下三个：1、响应状态码断言2、业务状态码断言3、数据的验证

用例场景设计：
430100       业务状态码：'ResultCode': 10001    数据验证：'ErrorInfo': '城市信息获取成功'
430100mn     业务状态码：'ResultCode': 20104    数据验证：'ErrorInfo': '获取城市信息过程中出现异常：无效的 JSON 基元: 430100mn。'
为空          业务状态码：'ResultCode': 20104    数据验证：'ErrorInfo': '获取城市信息过程中出现异常：无效的 JSON 基元: 。'
123123123213123，业务状态码：'ResultCode': 20103  数据验证：'ErrorInfo': '未找到数据源'
'''

# python  +  unittest  + requests + jenkins
import unittest, requests, json

class CityCodeApi(unittest.TestCase):

    def setUp(self):
        self.url = 'http://183.62.167.17:10158'
        self.path = '/CyzgMobileConfigService/GetDataInfo'
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def tearDown(self):
        pass

    def test_01right_citycode(self):
        '''查询城市编码API-正常的接口测试用例'''
        payload = {'CommandCode': 'GetAllCityData',
                   'Marker': '1482738389646',
                   "TransferData": "{\'CityId\':430100}"}
        try:
            r = requests.post(self.url+self.path, json=payload, headers=self.headers)
            # assertEqual第三个参数表示断言错误显示的信息
            self.assertEqual(r.status_code,200,'提示：状态码不是200')
            self.assertEqual(r.json()['ResultCode'],10001,'提示：业务状态码不是10001')
            self.assertEqual(r.json()['ErrorInfo'],'城市信息获取成功','提示：数据验证失败')
        except Exception as message:
            print('接口请求出错！出错的原因：{}'.format(message))

    def test_02error_citycode(self):
        '''查询城市编码API-城市ID为空的接口测试用例'''
        payload = {'CommandCode': 'GetAllCityData',
                   'Marker': '1482738389646',
                   "TransferData": "{\'CityId\':}"}
        try:
            r = requests.post(self.url+self.path, json=payload, headers=self.headers)
            self.assertEqual(r.status_code,200,'提示：状态码不是200')
            self.assertEqual(r.json()['ResultCode'],20104,'提示：业务状态码不是20104')
            self.assertEqual(r.json()['ErrorInfo'],'获取城市信息过程中出现异常：无效的 JSON 基元: 。','提示：数据验证失败')
        except Exception as message:
            print('接口请求出错！出错的原因：{}'.format(message))

    def test_03error_citycode(self):
        '''查询城市编码API-城市ID为空的接口测试用例'''
        payload = {'CommandCode': 'GetAllCityData',
                   'Marker': '1482738389646',
                   "TransferData": "{\'CityId\':11111}"}
        r = requests.post(self.url+self.path, json=payload, headers=self.headers)
        self.assertEqual(r.status_code,200,'提示：状态码不是200')
        self.assertEqual(r.json()['ResultCode'],20103,'提示：业务状态码不是20103')
        self.assertEqual(r.json()['ErrorInfo'],'未找到数据源')


if __name__ == '__main__':
    unittest.main(verbosity=2)


