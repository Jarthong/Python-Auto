
# 创建一个txt文件
filename = open('D:\data.txt','w',encoding='UTF-8')
filename.write('我们都是好孩子\n我爱Python\n我爱Java\n我爱JavaScript')
filename.close()
print('检查文件是否被正常关闭',filename.closed)

# 读取文件的几种方式
# read
# file = open('D:\data.txt','r',encoding='utf-8')
# # print('read读取文件内容展示：\n',file.read())
# # print('read读取文件内容展示：\n',file.read(5))

# readline 默认读取第一行
m = file.readline()
print(m)

# redadlines 读取所有内容，并将结果存储到列表中
print(file.readlines())

# for循环迭代文件
for read in file:
    print(read,end='')

# writelines
file = open('data2.txt','w',encoding='utf-8')
list1 = ['我们都是好孩子\n','我爱Python\n','我爱Java\n','我爱JavaScript\n']
file.writelines(list1)
file.close()
file1 = open('data.txt','r',encoding='utf-8')
print(file1.read())


with open('data3.txt','a',encoding='utf-8') as f:
    f.writelines([
        '我们都是好孩子\n'
        '我爱Python\n'
        '我爱Java\n'
        '我爱JavaScript\n'
    ])
print('检查文件是否被正常关闭',f.closed)

with open('data3.txt','r',encoding='utf-8') as f1:
    print(f1.read())


# 使用for循环 文件读写 函数 本地创建10文件
def creat_txt():
    path = r'E:\demo_create\\'   # 也可以写成 path = 'E:\\demo_create\\' (每个\都要转义)
    for text in range(1,11):
        with open(path + str(text) + '.txt','w',encoding='utf-8') as f:
            f.write(str(text)+'1')
creat_txt()

