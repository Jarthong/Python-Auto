# 序列化和反序列化
# 序列化：将Python对象转换为json数据（json字符串）   json.dumps（）
# 反序列化：将json数据（json字符串）转换为Python对象 json.loads()

# 字典的序列化和反序列化实例:
import json
dict = {'name': 'jarthong', 'phone': '15915773544', 'address': '深圳'}
print('序列化前的数据类型是{} \n序列化前的数据是{}'.format(type(dict),dict))
print('-'*100)

# 对dict进行序列化操作
str_dict = json.dumps(dict)
print('序列化后的数据类型是{} \n序列化后的数据是{}'.format(type(str_dict),str_dict))
print('-'*100)
# 解决中文乱码
str_dict4 = json.dumps(dict,ensure_ascii=False)
print('解决中文乱码后的数据类型是{} \n解决中文乱码后的数据是{}'.format(type(str_dict4),str_dict4))
print('-'*100)


# json格式的数据格式化输出,indent表示缩进,sort_keys=True表示按照ASCII码表排序
str_dict2 = json.dumps(dict,indent=4,sort_keys=True)
print('格式化后的数据类型是{} \n格式化后的数据是{}'.format(type(str_dict2),str_dict2))
print('-'*100)
# 解决中文乱码
str_dict3 = json.dumps(dict,indent=4,sort_keys=True,ensure_ascii=False)
print('解决中文乱码后的数据类型是{} \n解决中文乱码后的数据是{}'.format(type(str_dict3),str_dict3))
print('-'*100)

# 对str_dict2进行反序列化
dict_str = json.loads(str_dict2)
print('反序列化后的数据类型是{} \n反序列化后的数据是{}'.format(type(dict_str),dict_str))
print('-'*100)


# 对列表、元组，都可以使用序列化和反序列号
list1 = ['name', 'jarthong', 'phone', '15915773544', 'address', '深圳']
print('序列化前的数据类型是：{}\n序列化前的数据是：{}'.format(type(list1),list1))
print('-'*100)

list1_str = json.dumps(list1, indent=4, sort_keys=True)
print('序列化后的数据类型是：{}\n序列化后的数据是：{}'.format(type(list1_str),list1_str))
