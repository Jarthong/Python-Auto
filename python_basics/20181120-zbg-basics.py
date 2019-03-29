'''
# 字典key值根据降序排序，并生成一个数组，sorted()
a = {'nane': 'jarthong', 'age': '27', 'sex': 'boy', 'phone': '15915773544'}
b = sorted(a)
print(type(b), b)
print('根据key输出value：', a['age'])
print('-'*100)
# 参数内容拼串：所有参数按key值首字母排序后再按key1+value1+key2+value2...的形式拼串
param = ''
for k in sorted(a):
    print('key值是：', k)
    print('value值是:', a[k])
    # param = k + a[k]
    # param = param + k + a[k]
    param += k + a[k]
    print('拼接的字符串是：', param)
    print('-'*50)
print('-'*100)
print('最终拼接的字符串是：', param)


# "XX if A else YY"语法，如果是A的话，执行XX,否则执行YY
import random
a = random.randint(0, 9)
b = 'xx' if a == 5 else 'yy'
print(b)
# 以上语句与以下语句相同
if a == 5:
    b = 'xx'
else:
    b = 'yy'
print(b)
'''













