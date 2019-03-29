'''
from selenium import webdriver
d = webdriver.Chrome()
d.get('http://192.168.133.129/ecshop/user.php')

import time
a = b'123456789'
print(type(a))
b = a.decode('utf-8')
print(b)


timestamp = str(int(time.time() * 1000))
print(timestamp)

rob_url = '/exchange/activity/controller/zbgactivitycontroller/inputFund'
param_rob = {'inputType': '7lEGtD2Q4g5','amount': 20,'googleCode': 1}
# r_rob = requests.post(url=base_url+rob_url, headers=headers_rob, data=param_rob, verify=False)
# print(r_rob.json())




import requests, hashlib, json
import time
import json
import base64
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
import time

payload = {'inputType': '7lEGtD2Q5E3', 'amount': '23', 'googleCode': '33'}
# inputType=ieo_id,googleCode=google_code, amount=amount
print(payload, type(payload))
print(sorted(payload),type(sorted(payload)))
param = ''
for k in sorted(payload):
    param += k + payload[k]
print(param, type(param))
'''


def test(**params):
    return params
    # print(params, type(params))

dict_1 = test(B='womem', C='jarthong', A='18')
sorted_1 = sorted(dict_1)
print('dict_1是：', dict_1, type(dict_1))
print('sorted_1是：', sorted_1, type(sorted_1))
param = ''
print(dict_1)
for i in sorted(dict_1):
    param += i + dict_1[i]
    print(param)
