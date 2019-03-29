import datetime
from time import *

print('打印当前系统时间:', datetime.datetime.today())

sleep(0)
print('打印当前系统时间:', datetime.datetime.now())

t = datetime.datetime(2018, 6, 8, 9, 53, 30)
# t = datetime.datetime.now()
print('打印自定义的时间：', t)
print('打印自定义的时间（年份）：', t.year)
print('打印自定义的时间（月份）：', t.month)
print('打印自定义的时间（日期）：', t.day)
print('打印自定义的时间（小时）：', t.hour)

t1 = datetime.date(2018, 12, 12)
print('打印自定义日期：{}'.format(t1))
print('打印自定义日期（年份）：{}'.format(t1.year))
print('打印自定义日期（月份）：{}'.format(t1.month))

t2 = datetime.time(12,25,23)
print('打印自定义时间：{}'.format(t1))
print('打印自定义时间（小时）：{}'.format(t2.hour))
print('打印自定义时间（分钟）：{}'.format(t2.minute))
print('打印自定义时间（秒钟）：{}'.format(t2.second))

s = '2018-6-8'
print(type(s))
s_new = datetime.datetime.strptime(s,'%Y-%m-%d')
print(s_new)

s1 = datetime.datetime.now()
s2 = datetime.date(2018,6,8)
print(type(s1))
s1_new = s1.strftime('%Y/%m/%d')
print(type(s1_new))
print(s1_new)
s2_new = s2.strftime('%Y-%m-%d')
print(s2_new)

print(datetime.datetime.strptime('2018-6-8','%Y-%m-%d'))
print(datetime.datetime(2018,6,8,12,25,36).strftime('%Y-%m-%d '))

print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))