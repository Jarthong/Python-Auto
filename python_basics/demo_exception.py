# 忽略所有异常，重新循环
while True:
    try:
        x = int(input('请输入一个数字：'))
        print('jarthong')
        break
    except Exception as message:
        a = 1+2
        print('Oops! That was no valid number.Try again',message)
        print(a)

'''
# 忽略指定的异常，重新循环
while True:
    try:
        x = int(input('请输入一个数字：'))
        print('jarthong')
        break
    except ValueError:
        print('Oops! That was no valid number.Try again')

# try:
#     name = '深圳'
#     print(name)
# except:
#     print('代码有误！抛出异常！')

# age = 123
# # name = 'jarthong'
# print(name+str(age))
#
# try:
#     m = input('请输入一个文件：')
#     f = open(m,'r',encoding='utf-8')
#     print(f.read())
# except Exception as message:
#     print(message)
# finally:
#     print('不管如何，我都执行！')


def div(c,d):
    print(c/d)


def divsion(a,b):
    if b == 0:
        raise Exception('分母不能为零！')
    else:
        print(a/b)


# divsion(9,0)


name = input('请输入你的名字：')
if name == 'stop':
    raise Exception('输入有误！')
else:
    print('Hello,{}!'.format(name))



'''
