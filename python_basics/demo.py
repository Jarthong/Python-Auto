
# 查看变量的内存位置
a = 3.1
print(id(a))
print(type(a))

b = False
print(type(b))

c = 'jarthong'
print(type(c))

number = 99
number1 = float(number)
print(number1)
number2 = int(number1)
print(number2)
number3 = str(number)
print(number3)
print(type(number3))
number4 = float(number3)
print(type(number4))

print(dir(str))
# a = 这是一段多行注释\t你看见了吗？
print(a)

path = r'E:\n软件测试资料\自动化提高班'
print(path)

name = 'jarthong'
age = 28
m = name + '的年龄是:' + str(age)
print(m)

# print('{m}的年龄是{n}'.format(m = a,n = b))

a = 'jarthong'
b = -1.8
print('%s的年龄是%s' %(a, b))
print(isinstance(b,float))


print('jarthong\n'*10)


a = 'ja_rt_hong'
print(a.find('_'))
b = a.split('_')[1]
print(type(b))
print(b)

c = a.replace('_hong','love')
print(c)



list = [1,5,9,'jarthon',1.55,'hong',9]
# a = list[::-1]
# print(a)
print(list)
# list.insert(2,'love')
# print(list)

list.remove(9)
print(list)

del list[-1]
print(list)


list = ['2',1,3]
list2 = ['jarthon',2]
print(list<list2)


name = 'womendoushihaohaizwoaini'
list = [1,5,9,66,[1.55,[555,9]]]
print(list.count(9))
print(len(list))
print(len(name))
# list.sort()
print(list)
a = list[-1][-1]
print(a)


tuple = (1,)
print(type(tuple))


list = [1,5,9,66]
# a = tuple(list)
print(tuple(list))


a = {'name':'jarthong','sex':'boy','age':27,'address':'深圳','tel':'15915773544'}

print(a.keys())
print(a.values())
print(a.items())
print('address' in a)
if 'address' in a:
    print('我爱你！')
else:
    print('我不爱你！')

print(a['sex'])
c = a['name']
print(c)
b = a.get('name')
print(b)
a['sex'] = 'gril'
print(a)
a['sex'] = a['name']
print(a)


a = {'name':'jarthong','sex':'boy','age':27,'address':'深圳','tel':'15915773544'}
print(a)
b = {'身高':170,'血型':'O'}
a.update(b)
print(a)
print(b)

a = {'name':'jarthong','sex':'boy','age':27,'address':'深圳','tel':'15915773544'}
print('学生信息 姓名%s 年龄%s 电话%s' %(a['name'],a['age'],a['tel']))
print('学生信息 姓名{} 年龄{} 电话{}'.format(a.get('name'),a.get('age'),a.get('tel')))

a = {'name','sex','boy','age',27,'address','深圳','tel','15915773544'}
b = {'name','sex','age',27,'address','广州','love','15915773544'}
# print(type(a))
# print(a)
# a.add('love')
# print(a)
# a.remove('tel')
# print(a)
c = a | b
print(c)
d = a & b
print(d)


num1 = 88
num2 = 3
c = num1/num2
print(c)

print('hed' not in 'hello')
assert 2 != 1,'2不等于1'

name = str(input('请输入你的名字'))
if name.endswith('俊雄'):
    if name.startswith('洪'):
        print('hello,%s' %name)
    elif name.startswith('林'):
        print('你不是主人，bye-bye %s' %name)
    else:
        print('滚犊子：%s' %name)
else:
    print('你输入错误！')


m = 80.5
h = 1.75
BMI = m/(h*h)
print(BMI)

m = float(input('请输入您的体重（单位为kg）'))
h = float(input('请输入您的身高（单位为m）'))
BMI = m/(h*h)
print(BMI)
if BMI <= 18.5:
    print('您的体重太轻了')
elif BMI>18.5 and BMI<=25:
    print('您的体重输入正常范围')
elif BMI > 25 and BMI <= 28:
    print('您的体重过重了')
elif BMI > 28 and BMI <= 32:
    print('您已经属于肥胖了')
elif BMI > 32:
    print('您已经输入严重肥胖了')
else:
    print('您输入有误')


message = 'hello,python!'
a = {'name':'jarthong','sex':'boy','age':27,'address':'深圳','tel':'15915773544'}
# for i in a.values():
#     # print('当前打印的是:%s' %i)
#     print('当前打印的是:{}'.format(i))
for i in enumerate(a):
    print(i)

a = ['name','jarthong','sex','boy','age','address','深圳','tel','15915773544']
print('列表内元素的个数',len(a))
# for i in range(len(a)):
#     print(i)
for i in range(len(a)):
    print('当前打印的元素是',a[i],'它的长度是',len(a[i]))


for i in range(1,10):
    print('-----',i)
    for j in range (1,10):
        print('+++++',j)


for i in range(1,10):
    print('----',i)
    for j in range(1,i+1):
        print('++++++',j)
        if j == 5:
            break

a = 'brtctesting.com'
b = 'www.brtctesting.com'
list = []
# print('list列表中的值变成了%s' %list)
for i in b:
    if i not in list:
        list.append(i)
    print(list)

found = False
for i in range(9):
    if i==6:
        found = True
        print('找到了')
        print(found)
        break
    else:
        print('没找到！！')

for i in range(9):
    print('现在演示的是for循环的计数循环次数，打印Python')

URL = 'www.brtctesting.com'
while URL:
    print(URL)
    URL = URL[1:]

a,b = 1,10
while a < b:
    print(a)
    a += 1
else:
    print('条件不满足，执行下面的代码块')
    print(a)
a = 10
while a:
    a -= 1
    if a % 2 != 0:
        continue
    print(a)


while True:
    name = input('请输入您的姓名：')
    if name == 'stop':
        break
    age = input('请输入您的年龄：')
    print('您好！{}，您的年龄是{}，欢迎您学习自动化教程！'.format(name,age))

import random
number =  random.randint(1,10)
print(number)


import random
number = input('你猜一个1到10的输入')
while True:
    if number == random.randint(1,10):
        print('你猜对了')
        break
    else:
        print('你猜错了')
        number = int(input('请重新输入数字：'))











