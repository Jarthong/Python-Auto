import random
'''x
# 从括号中的字符中取随机其中一个字符
m = random.choice('abcdefghijklmmopqrstuvwxyz')
# 从括号中的字符中取随机其中一个字符，组成一份数组
n = random.choices('abcdefghijklmmopqrstuvwxyz')
print(type(m), m)
print(type(n), n)
'''

# 从已知数字中随机取值
list_num = [2, 3.3, 5.6, 7, 12, 24.3, 45, 14.8]
number_choice = random.choice(list_num)
print('random.choice(list_num)随机取值是：', number_choice)

'''
# 获取参数间的整数，头尾都包含
number_randint = random.randint(1, 10)
print('random.randint(1,10)生成的随机数是：', number_randint)

# 获取参数间的整数，头尾不包含
number_randrange = random.randrange(1, 10)
print('random.randrange(1, 10)生成的随机数是：', number_randrange)

# 获取0-1间的浮点数
number_random = random.random()
print('random.random()生成的随机数是：', number_random)

# 获取范围内的浮点数
number_uniform = random.uniform(5, 10)
print('random.uniform(5,10)生成的随机数是：', number_uniform)
# 生成n位小数的随机数，控制随机数的精度round(数值，精度)
number_round = round(number_uniform, 2)
print('生成2位小数的随机数是：', number_round)


import uuid
# 生成一个随机uuid.UUID
a = uuid.uuid4()
print(type(a),a)
# 生成一个随机字符串
b = str(uuid.uuid4())
print(type(b),b)

'''
