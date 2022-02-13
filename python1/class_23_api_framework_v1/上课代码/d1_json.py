import json

data = '{"mobile_phone":"18111111111","pwd":null}'
# a = eval(data)
# print(a)
# python中没有null的定义，eval无法转化
# json和字典的转化尽量不用eval

# 使用json模块完成转换
# loads表示把json 字符串 转换为字典
# json格式中的key必须用双引号，不能用单引号
data_dict = json.loads(data)
print(data_dict)

# 字典转化为json
data_dict = {'name':'yuz','pwd':None}
json_data = json.dumps(data_dict)
print(json_data)