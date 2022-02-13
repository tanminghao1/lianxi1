# 获取绝对路径下的文件夹路径及名称
import os

dir_name = os.path.dirname(os.path.abspath(__file__))
# 拼接一个路径
xianren = os.path.join(dir_name, 'xianren/xianren.txt')
# # 只读一行
# f = open(xianren,mode='rt',encoding='utf-8')
# print(f.readline())
# f.close()
#
# # 读取所有行
# f = open(xianren,mode='r',encoding='utf-8')
# print(f.readlines())
# f.close()

# f = open(xianren,mode='r',encoding='utf-8')
# while True:
#     line = f.readline()
#     # 如果没有行了
#     if not line:
#         # 空行也是有换行符的
#         break
#     print(line)
# f.close()
# readlines()

f = open(xianren,mode='r',encoding='utf-8')
# print(f.readlines())

a = f.readlines()
for i in a:
    # end,以空结尾，去掉换行
    print(i,end='')
