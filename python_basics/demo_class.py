
# 定义类的方法
'''
class Student:
class Student():
'''''
class Student(object):
    pass


c = Student()
print(c)
c.name = 'jathong'
c.age = '28'
print('访问Student类下面的name属性',c.name)

# 函数 面向过程

import datetime
dict_all = {'tile':'pyhon',
            'price':12.8,
            'auther':'jathong',
            'publiser':'北京大学出版社',
            'date':datetime.datetime.now()
            }

def find_book(dict_all):
    print(dict_all.get('tile'))
    print(dict_all.get('price'))
    print(dict_all.get('auther'))
    print(dict_all.get('publiser'))
    print(dict_all.get('date'))

find_book(dict_all)


# 类 面向对象
import datetime
class Find_book:
    def __init__(self,title,price,auther,publiser,publisdate):
        self.title = title
        self.price = price
        self.auther = auther
        self.publiser = publiser
        self.publisdate = publisdate

book = Find_book('python',28.6,'jarthong','北京出版社',datetime.datetime.now())
print('面向对象实现一个查找数的信息的过程：',book)
print(book.title)
print(book.price)
print(book.auther)
print(book.publiser)
print(book.publisdate)


# 子类继承父类的方法，子类定义自己的方法并访问
class Count:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

class MyCount(Count):
    def sub(self):
        return self.a - self.b

C = MyCount(55,65)
print('子类继承父类方法，使用父类add的方法，计算结果为：',C.add())
print('子类自己的方法，使用sub，计算结果为：',C.sub())

# 类的重写：子类对父类进行修改，不改变父类原有的属性，在此基础上增加
class MyCount_1(Count):
    def __init__(self,a,b,c):
        Count.__init__(self,a,b)
        self.c = c

    def sub(self):
        return self.c - self.b - self.a

c = MyCount_1(5,2,5)
print('修改父类,调用修改后子类的sub方法，计算结果为：',c.sub())
print('修改父类，调用父类原有add方法，计算结果为：',c.add())  # 只有两个使用a,b两个参数相加



# 类的应用
class Jisuan(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        if type(self.a) != int or type(self.b) != int:
            raise Exception('请输入整型！')
        return self.a + self.b

    def divide(self):
        if type(self.a) != int or type(self.b) != int:
            raise Exception('请输入整型！')
        if self.b == 0:
            raise Exception('除数不能为零！')
        return self.a / self.b

c = Jisuan(5,88)
# print(c.add())
print(c.divide())


class Student():
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def jieshao(self):
        print('我的名字是{}，我来自{}'.format(self.name,self.city))

    def talk(self):
        print('Hello,Anybody')

student1 = Student('jathong','shenzhen')
student1.jieshao()
student1.talk()