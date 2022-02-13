
# yaml格式
# {"languange":['ruby','perl','python'],"websites":{"YAML":"yaml"}}

import yaml
# 读取yaml配置
# 先打开yaml文件获取对象
# yaml中有中文，需要加编码格式
f = open('python25.yaml',encoding='utf-8')
# 读取到的yaml数据使用yanl.load()方法转化为python格式数据
data = yaml.load(f.read(),Loader=yaml.FullLoader)
print(data)
# 手动关闭
f.close()

# # 使用with open，不需要手动关闭文件
# with open('python25.yaml') as f:
#     data = yaml.load(f.read(),Loader=yaml.FullLoader)