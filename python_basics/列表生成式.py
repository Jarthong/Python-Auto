'''
lists = ['2018_result.html', '20_48_28_result.html','jarthong','hong.html','85566']
print(lists)
lists.sort()
print(lists)
filte = [x for x in lists if x.endswith('.html')]
print(filte)

import time
now_time = time.strftime('%Y-%m-%d-%H-%M')
print(now_time)

def user_login(username='jarthong', password='h123456'):
    print(username+password)

user_login()
user_login('洪俊雄','888888')
user_login('888888','洪俊雄')
user_login(username='洪俊雄',password='888888')
user_login(password='888888',username='洪俊雄')
'''
# 反转数组
a = [1,2,3,4,5,6]
a.reverse()
print(a)

