import os

print(os.path.abspath('.'))
print(os.path.abspath('..'))

print(os.path.dirname(os.path.realpath(__file__)))

print(os.listdir())

# os.path.join(a,b)
# cur_path = os.path.dirname(os.path.realpath(__file__))
cur_path = os.path.abspath('.')
print(cur_path)
join_path = os.path.join(cur_path,'dat.txt')
print(join_path)


m = r'E:\Python-test\demo\demo_os.py'
n = os.path.split(m)
print('拆分后的结果为：{}'.format(n))
print(n[-1])

i = os.path.splitext(m)
print(i[-1])

m = r'E:\Python-test/meng\\woeojm\demo\demo_os.py'
print(os.path.normpath(m))


print(os.sep)
print(os.pathsep)
print(os.curdir)
print(os.pardir)

print(os.getcwd())
# os.chdir(r'E:\Python-test\menu')
print(os.getcwd())
# os.mkdir(r'E:\Python-test\menu\test')
print(os.listdir())

with open(r'E:\Python-test\menu\test.txt','w',encoding='utf-8') as f:
    f.write('')

os.rename(r'E:\Python-test\menu\test_rename.txt',r'E:\Python-test\menu\test.txt')

os.remove(r'E:\Python-test\menu\test.txt')
os.rmdir(r'E:\Python-test\menu')

import os
# os.path.isdir('目录路径') 判断一个目录是否为目录，是返回Ture，不是返回False
m = os.path.isdir(r'E:\Python-test\demo1.py')
print(m)
# os.path.isfile('文件路径+文件名') 判断一个文件是否为文件，是返回Ture，不是返回False
n = os.path.isfile(r'E:\Python-test\demo1.py')
print(n)

path = 'E:\\Python-test\\python_selenium\\unittest_project\\report'
lists = os.listdir(path)  # 列出path目录下面的所有文件和目录
print(lists)





