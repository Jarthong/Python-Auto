'''
def read_book():
    print('拿起一本本书！')
read_book()

def learning(name,course,start,end):
    print('{}学习了《{}》'.format(name,course))
    print('课程从第{}章学习到了第{}章'.format(start,end))
    print('{}学习结束'.format(name))

learning('jarthong','自动化',2,5)


def add(a,b):
    result = a + b
    # print(result)
    return result
print(add(8,15))

c = 100
m =  c + add(88,99)
print(m)

def studentinfo(name,age,sex,address='深圳'):
    print('Hello {},My age is {}'.format(name,age))
    print('欢迎你来到中国哦！'+'过来一起吃饭吧！')
    print('我来自{}'.format(address))
studentinfo(age='25',name='jatthong',sex='男',address='北京')


def studentinfo(name,age,sex,address='北京',**args):
    print('----打印学生信息表----')
    print('学生的姓名：{}'.format(name))
    print('学生的年龄：{}'.format(age))
    print('学生的性别：{}'.format(sex))
    print('家庭住址：{}'.format(address))
    print('其他信息：{}'.format(args))

dict1 = {'爱好':'唱歌','手机号码':'15915773544','语言':'Python'}

studentinfo('jarthong',28,'男','深圳',**dict1)

def hello_chinese(name):
    print('你好!{}'.format(name))
def hello_english(name):
    print('Hello!{}'.format(name))
def hello_japanese(name):
    print('kon ni qi wa!{}'.format(name))

while True:
    name = input('请输入你的名字')
    if name == '日本':
        break
    language = input('请输入你要实现的打招呼版本：\n'
                     '1.输入c代表的是中文版\n'
                     '2.e\n'
                     '3.j\n'
                     '请开始你的表演')
    if language == 'c':
        hello_chinese(name)
    if language == 'e':
        hello_english(name)
    if language == 'j':
        hello_japanese(name)
'''

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mutil(e,f):
    return e * f
def divide(g,h):
    return g / h

def Jisuan_Calc():
    while True:
        m = input('请选择你要做的运算：（+、—、*、/）')
        if m not in ['+','-','*','/']:
            print('你输入有误，请重新输入：')
        else:
            a = float(input('亲输入第一个数字：'))
            b = float(input('请输入第二个数字：'))
            if m == '+':
                print('加法运算，运算结果为：{}'.format(add(a,b)))
                check = input('请问还要继续其他运算吗？\n“y”表示要，“n”表示不要。\n请输入：')
                if check == 'n':
                    break
                else:
                    continue
            elif m == '-':
                print('减法运算，运算结果为：{}'.format(sub(a,b)))
                check = input('请问还要继续其他运算吗？\n“y”表示要，“n”表示不要。\n请输入：')
                if check == 'n':
                    break
                else:
                    continue
            elif m == '*':
                print('乘法运算，运算结果为：{}'.format(mutil(a,b)))
                check = input('请问还要继续其他运算吗？\n“y”表示要，“n”表示不要。\n请输入：')
                if check == 'n':
                    break
                else:
                    continue
            elif m == '/':
                print('除法运算，运算结果为：{}'.format(divide(a,b)))
                check = input('请问还要继续其他运算吗？\n“y”表示要，“n”表示不要。\n请输入：')
                if check == 'n':
                    break
                else:
                    continue


def count_str(str):
    j = 0
    for i in str:
        j += 1
    return j
    # return len(str)

m = input('请输入一个字符串')
print(count_str(m))














